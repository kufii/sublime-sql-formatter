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
