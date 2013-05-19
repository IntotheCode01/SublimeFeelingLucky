#
# SublimeFeelingLucky.py
#
# v 0.1
#

import sublime, sublime_plugin, re, os, json, time

_word = ""
_prefix = ""

class FeelingLucky(sublime_plugin.TextCommand):

	def run(self, edit):
		global _prefix
		global _word

		projectPath = sublime.active_window().folders()[0]

		if not _check(self, -4, "html") :
			_showAlert("html file only")
			return

		# get Json data
		data = self.loadJSON()
		if not data :
			return

		for region in self.view.sel():
			_word = self.view.substr(self.view.word(region))
			line = self.view.substr(self.view.line(region))

			match = re.search(r'.+(id|class).+', line)
			if match is None:
				_showAlert("Not match 'id' or 'class'")
				return
			else:
				type = match.group(1)
				if   type == "id" 	 : _prefix = "#"
				elif type == "class" : _prefix = "."

			count = 0

			# check css
			if "css" in data :
				for css in data["css"] :
					count += 1
					cssFile = os.path.join(projectPath, css)
					if os.path.isfile(cssFile) :

						# TODO
						# Already Open file move

						print self.view.window()
						self.view.window().run_command('expand_and_focus_right_panel', { "len": len(data["css"]), "count": count })
						cssView = self.view.window().open_file(cssFile)
						cssView.window().set_view_index(cssView, count, 0)
					else :
						_printError("Not found " + css)

			# check sass
			if "sass" in data :
				for sass in data["sass"] :
					count += 1
					sassFile = os.path.join(projectPath, sass)
					if os.path.isfile(sassFile) :
						sassView = self.view.window().open_file(sassFile)
						sassView.window().set_view_index(sassView, count, 0)
					else :
						_printError("Not found " + sass)


	def loadJSON(self) :
		try:
			f = open(os.path.join(sublime.active_window().folders()[0], "config.feelinglucky"))
			data = json.load(f)
			f.close()
			return data
		except Exception, e:
			if sublime.ok_cancel_dialog('Not found config.feelinglucky\nMake config.feelinglucky file ?') :
				self.view.run_command("make_config_dot_feeling_lucky")
			return False


#
# css file
#
class FeelingLuckyCssFile(sublime_plugin.TextCommand):

	def run(self, edit):

		if not _check(self, -3, "css") :
			return

		text = _prefix + _word
		match = self.view.find(text, 0, sublime.LITERAL)
		if match :
			self.view.sel().clear()
			self.view.sel().add(match)
			self.view.show(match)

		else :
			# TODO
			# not match file close
			return


#
# event
#
class FeelingLuckyEventListener(sublime_plugin.EventListener):

	def on_load(self, view):
		self.call(view)

	def on_activated(self, view):
		self.call(view)

	def call(self, view):
		view.run_command("feeling_lucky_css_file")


#
# config.feelinglucky
#
class MakeConfigDotFeelingLucky(sublime_plugin.TextCommand):

	def run(self, edit):

		if os.path.isfile(os.path.join(sublime.active_window().folders()[0], "config.feelinglucky")) :
			_showAlert("Found config.feelingLucky")

		else :
			print 'Make config.feelingLucky'
			config = { "sass":[], "css":["style.css"] }
			file = open(os.path.join(sublime.active_window().folders()[0], "config.feelinglucky"), "w")
			json.dump(config, file, indent=4)


#
# window controll
#
class ExpandAndFocusRightPanel(sublime_plugin.WindowCommand):

	def run(self, len, count):
		w = 0.6;

		if len == 1:
			p = {
					"cols": [0.0, w, 1.0],
					"rows": [0.0, 1.0],
					"cells":
					[
						[0, 0, 1, 1], [1, 0, 2, 1]
					]
				}
		elif len == 2 :
			p = {
					"cols": [0.0, w, 1.0],
					"rows": [0.0, 0.5, 1.0],
					"cells":
					[
					    [0, 0, 1, 2], [1, 0, 2, 1],
					                  [1, 1, 2, 2]
					]
				}
		elif len >= 3 :
			p = {
					"cols": [0.0, w, 1.0],
					"rows": [0.0, 0.33, 0.66, 1.0],
					"cells":
					[
					    [0, 0, 1, 3], [1, 0, 2, 1],
					                  [1, 1, 2, 2],
					                  [1, 2, 2, 3]
					]
				}

		self.window.run_command("set_layout", p)
		self.window.run_command("focus_group", {"group": count})


#
# utils
#

def _showAlert(message) :
	sublime.error_message("SublimeFeelingLucky : \n" + message)

def _printError(message) :
	print "[FeelingLucky Error] : " + message

# file type check
def _check(self, range, type) :
	fileName = self.view.file_name()
	if fileName[range:] == type :
		return True
	else :
		return False





