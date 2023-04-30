import sublime
import sublime_plugin
import os

from .src import formatter, preferences


class SqlFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):  # pylint: disable=arguments-differ
        self.syntax_to_sql()
        self.format(edit, **kwargs)

    def syntax_to_sql(self):
        syntax = os.path.splitext(os.path.basename(self.view.settings().get("syntax")))[0]
        if syntax.lower() != "sql" and preferences.get_pref('set_syntax_on_format'):
            self.view.set_syntax_file("Packages/SQL/SQL.sublime-syntax")

    def format(self, edit, **kwargs):
        full_file_region = sublime.Region(0, self.view.size())
        file_text = self.view.substr(full_file_region)
        formatted_text = formatter.format_sql(file_text, kwargs['dialect'] if kwargs else None)

        if not formatted_text or formatted_text == file_text:
            return

        self.view.replace(edit, full_file_region, formatted_text)


class SqlFormatterDialectSelect(sublime_plugin.TextCommand):
    def run(self, edit):
        dialects = {
            'sql': 'Standard SQL',
            'n1ql': 'Couchbase N1QL',
            'db2': 'IBM DB2',
            'pl/sql': 'Oracle PL/SQL'
        }

        def run_command(index):
            if index >= 0:
                dialect = list(dialects.keys())[index]
                self.view.run_command('sql_formatter', {
                    'dialect': dialect
                })
        self.view.window().show_quick_panel(list(dialects.values()), run_command, 0)
