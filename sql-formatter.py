import sublime
import sublime_plugin

from .src import formatter


class SqlFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):  # pylint: disable=arguments-differ
        dialect = kwargs['dialect'] if kwargs else None

        for region in self.view.sel():
            if region.empty():
                selection = sublime.Region(0, self.view.size())
                self.replace_region_with_formatted_sql(edit, selection, dialect)
            else:
                self.replace_region_with_formatted_sql(edit, region, dialect)
        
    def replace_region_with_formatted_sql(self, edit, region, dialect):
        selected_text = self.view.substr(region)
        formatted_text = formatter.format_sql(selected_text, dialect)

        if not formatted_text or formatted_text == selected_text:
            return
        
        self.view.replace(edit, region, formatted_text)


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
