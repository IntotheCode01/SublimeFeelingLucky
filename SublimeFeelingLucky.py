import sublime, sublime_plugin, re, os

_word = ""
_prefix = ""


def _showAlert(message) :
	sublime.error_message("SublimeFeelingLucky\n\n" + message)


class FeelingLuckyCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		global _prefix
		global _word

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


class FeelingLuckyCssFileCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		text = _prefix + _word
		match = self.view.find(text, 0, sublime.LITERAL)
		if not match:
			return

		self.view.sel().clear()
		self.view.sel().add(match)
		self.view.show(match)


class SublimeFeelingLuckyEventListener(sublime_plugin.EventListener):

	def on_load(self, view):
		call(view)

	def on_activated(self, view):
		call(view)

	def call(self, view):
		view.run_command('feeling_lucky_css_file')


# class MakeSublimeFeelingLuckyFile():
