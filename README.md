# sublime-sql-formatter

A Sublime Text plugin that runs the [cli-sql-formatter](https://github.com/kufii/cli-sql-formatter) node library on the current file. cli-sql-formatter is in turn a command line interface for the [sql-formatter](https://github.com/zeroturnaround/sql-formatter) node library.

## Installation

### Dependencies

This plugin requires node.js, and also requires cli-sql-formatter to be globally installed.

`npm install -g cli-sql-formatter`

### Plugin Installation

In the future, once approved, this plugin will be installable via [Package Control](https://packagecontrol.io/installation)

To install via Package Control, do the following:

1. Within Sublime Text, bring up the Command Palette and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `sql-formatter`. Among the entries you should see `sql-formatter`. Select this entry to install it.

## Commands

### Command Palette

* `Format SQL`: Runs the formatter with the default dialect defined in your settings.
* `Format SQL With Dialect`: Runs the formatter with a dialect of your choosing.

### Default Hotkeys

By default, these hotkeys will run the formatter with the default dialect defined in your settings.

* Linux/Windows: [Ctrl + KQ]
* Mac: [Cmd + KQ]

## Settings

By default the following settings are used:

```javascript
{
	// The paths to look for executables
	"paths": {
		"linux": [],
		"osx": [],
		"windows": []
	},

	// The default dialect to use for formatting
	// Options:
	// "sql" - Standard SQL
	// "n1ql" - Couchbase N1QL
	// "db2" - IBM DB2
	// "pl/sql" - Oracle PL/SQL
	"default_dialect": "sql",

	// The number of spaces to indent with
	"indent_size": 2,

	// Indent with tabs instead of spaces
	"use_tabs": false
}
```

You can modify any settings by going to Preferences > Package Settings > sql-formatter > Settings.

## Project-Specific Settings Override

To override global plugin configuration for a specific project, add a settings object with an `sql-formatter` key in your `.sublime-project`. This file is accessible via `Project -> Edit Project`.

For example:

```javascript
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"use_tabs": true
	}
}
```
