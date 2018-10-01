from subprocess import Popen, PIPE

import sublime

from . import preferences, pathutil


def _get_node_path():
    node = pathutil.find_executable(preferences.get_path(), 'node')
    if not node:
        raise Exception('Could not find Node.js. Check that your configuration is correct.')
    return node


def _get_sql_formatter_path():
    node = pathutil.find_executable(preferences.get_path(), 'cli-sql-formatter')
    if not node:
        raise Exception('Could not find cli-sql-formatter. Check that it is installed and that your configuration is correct.')
    return node


def format_sql(sql, dialect=None):
    cmd = None
    if sublime.platform() == 'windows':
        cmd = [_get_sql_formatter_path()]
    else:
        cmd = [_get_node_path(), _get_sql_formatter_path()]

    if not dialect:
        dialect = preferences.get_pref('default_dialect')

    if dialect:
        cmd.extend(['-d', dialect])

    if preferences.get_pref('use_tabs'):
        cmd.extend(['-t'])
    else:
        cmd.extend(['-i', str(preferences.get_pref('indent_size'))])

    print(cmd)

    return Popen(cmd, stdin=PIPE, stdout=PIPE, shell=(sublime.platform() == 'windows')) \
        .communicate(sql.encode('utf-8'))[0] \
        .decode('utf-8')
