import sublime, sublime_plugin, re, os, json

_word = ""
_prefix = ""

def _showAlert(message) :
	sublime.error_message("SublimeFeelingLucky\n\n" + message)


class FeelingLuckyCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		global _prefix
		global _word

		# load json
		f = open(sublime.active_window().folders()[0] + "/config.feelinglucky")
		data = json.load(f)
		f.close()
		print data
		print data[0]['css'][0]
		print data[0]['sass'][0]


		for region in self.view.sel():
			_word = self.view.substr(self.view.word(region))
			line = self.view.substr(self.view.line(region))

			match = re.search(r'.+(id|class).+', line)
			if match is None:
				_showAlert("Not match 'id' or 'class'")
				return
			else:
				type = match.group(1)
				if type == "id" 	 : _prefix = "#"
				elif type == "class" : _prefix = "."

			all = self.view.substr(sublime.Region(0, self.view.size()))
			cssmatch = re.findall(r'href="(.*?.css)', all)
			if cssmatch is None:
				_showAlert("Not found css file")
				return
			else:
				for file in cssmatch :
					sublime.active_window().open_file(file)


#
# css file
#
class FeelingLuckyCssFileCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		text = _prefix + _word
		match = self.view.find(text, 0, sublime.LITERAL)
		if not match:
			return

		self.view.sel().clear()
		self.view.sel().add(match)
		self.view.show(match)


#
# event
#
class SublimeFeelingLuckyEventListener(sublime_plugin.EventListener):

	def on_load(self, view):
		self.call(view)

	def on_activated(self, view):
		self.call(view)

	def call(self, view):
		view.run_command('feeling_lucky_css_file')


#
# config.feelinglucky
#
class MakeConfigDotFeelingLucky():
	print 'Make config.feelingLucky'



