import sublime, sublime_plugin
import re

class SqlAutoComplete(sublime_plugin.EventListener):
	def on_modified(self, view):
		print view.file_name() + " modified"  
		if ".sql" in view.file_name(): 
			view.run_command("replace_in_sql_snippet") 

	def on_query_completions(self, view, prefix, locations):
		print "on_query_completions"   
		return [ { "trigger": "a", "contents": "<a href=\"$1\">$0</a>" } ]
 
    

class ReplaceInSqlSnippetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		schema = self.get_schema() 
		schemaRegin = self.view.find("\{schema\}", 0, sublime.IGNORECASE)
		if schema and schemaRegin: 
			print self.view.substr(schemaRegin)
			self.view.replace(edit, schemaRegin, schema.upper())

		# sels = self.view.sel() 
		# for selection in sels:
		# 	print self.prefix_word(selection)
		# 	self.view.window().show_quick_panel(['a','b'], self.on_done(), sublime.MONOSPACE_FONT)

	def get_schema(self):
		useRegin = self.view.find("use ?.*;", 0, sublime.IGNORECASE) 
		if useRegin: 
			schema = re.compile("use ?(.*);", re.IGNORECASE).match(self.view.substr(useRegin)).group(1)
			return schema 
		return None 

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


