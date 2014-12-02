import sublime, sublime_plugin

class SqlAutoComplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		print [('a','b')]
		 

		return [
                { "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
                { "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
                { "trigger": "acronym", "contents": "<acronym>$0</acronym>" }
        ]

class AutoSqlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		for selection in sels:
			print self.prefix_word(selection)
			self.view.window().show_quick_panel(['a','b'], self.on_done(), sublime.MONOSPACE_FONT)

	def prefix_word(self, selection):
		begin = self.view.line(selection).begin()
		end = self.view.word(selection).end()
		return self.view.substr(sublime.Region(begin, end)).split(" ")[-1]

	def on_done(self):
		print ['a','b']
		 

class suggestion_panel(object):
	"""docstring for suggestionPopup"""
	def __init__(self, arg):
		super(suggestionPopup, self).__init__()
		self.arg = arg


