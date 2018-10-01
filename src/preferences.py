import os

import sublime

from . import pathutil


PLUGIN_NAME = 'sql-formatter'
SETTINGS_FILE = PLUGIN_NAME + '.sublime-settings'


def get_pref(key):
    default = sublime.load_settings(SETTINGS_FILE).get(key)
    custom_settings = sublime.active_window().active_view().settings()

    if custom_settings.has(PLUGIN_NAME):
        return custom_settings.get(PLUGIN_NAME).get(key, default)

    return default


def get_path():
    return map(pathutil.expand_path,
               filter(None,
                      get_pref('paths').get(sublime.platform()) +
                      os.environ.get('PATH', '').split(os.pathsep)))
