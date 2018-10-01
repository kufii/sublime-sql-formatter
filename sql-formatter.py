import sublime
import sublime_plugin

from .src import formatter


class SqlFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):  # pylint: disable=arguments-differ
        full_file_region = sublime.Region(0, self.view.size())
        file_text = self.view.substr(full_file_region)
        formatted_text = formatter.format_sql(file_text, kwargs['dialect'] if kwargs else None)

        if not formatted_text or formatted_text == file_text:
            return

        self.view.replace(edit, full_file_region, formatted_text)


class SqlFormatterDialectSelect(sublime_plugin.TextCommand):
    dialects = {
        'sql': 'Standard SQL',
        'n1ql': 'Couchbase N1QL',
        'db2': 'IBM DB2',
        'pl/sql': 'Oracle PL/SQL'
    }

    def run(self, edit):
        def run_command(index):
            if index >= 0:
                dialect = list(self.dialects.keys())[index]
                self.view.run_command('sql_formatter', {
                    'dialect': dialect
                })
        self.view.window().show_quick_panel(list(self.dialects.values()), run_command, 0)
