# pre-commit-hooks

This repository contains pre-commit hooks by Extenda Retail.

See also: http://pre-commit.com for general usage instructions.

To install the `pre-commit` module, Python 3 is required to be installed (tested OK with version 3.9.5). Make sure Python directory is placed in PATH. Python's Scripts directory also should be in PATH.

Run command to install `pre-commit`:

```sh
$ pip install pre-commit
```

Navigate to the project you want to apply pre-commit hooks and run:

```sh
$ pre-commit install
```

## Usage with pre-commit

Add this to your `.pre-commit-config.yaml` in project's root.

```yaml
default_stages: [commit]
-  repo: git://github.com/extenda/pre-commit-hooks
   rev: v0.13.0 # Use the ref you want to point at
   hooks:
   - id: google-java-formatter
   - id: commitlint
     stages: [commit-msg]
```

## Available hooks

* `eclipse-formatter` (__deprecated__) - Runs Eclipse Java formatter with default formatting rules on all staged `java` source files. The following arguments are available:
  * `--source` - set the Java compiler source version (default `1.8`)
  * `--target` - set the Java compiler target version (default `1.8`)
* `google-java-formatter` - Runs Google's Java formatter on all staged `java` source files. **Please note: Java 11 or newer is required in v0.5+** Use v0.4 if you need Java 8 support.
* `pre-commitlint` - Runs [commitlint](https://commitlint.js.org) to validate commit messages.
* `vale` (__deprecated__) - Runs [Extenda docker-vale](https://github.com/extenda/docker-vale) wrapping [Vale lint](https://github.com/errata-ai/vale) and Extenda's own lint style to validate natural language in files.

## Google Java format in your IDE

There's a Google Java Format plugin for both Eclipse and IntelliJ.

The current version used is `1.25.2`.

### Eclipse

[Download the formatter plugin](https://github.com/google/google-java-format/releases/download/google-java-format-1.6/google-java-format-eclipse-plugin_1.6.0.jar) and drop it into Eclipse's `dropins` folder.

The plugin adds a `google-java-format` formatter implementation that can be configured in `Window > Preferences > Java > Code Style > Formatter > Formatter Implementation` for the whole workspace.

If you have multiple projects in one workspace, it is possible to apply the formatter only to selected projects.

1. Navigate to `Window > Preferences > Java > Code Style > Formatter > Formatter Implementation`
2. Click on `Configure Project Specific Settings`
3. Select the project you want to apply the formatter
4. In a newly appear window check the checkbox on `Enable project specific settings`
5. Select `google-java-format` in a drop-down menu `Formatter implementation`
6. Save

You must also change `Window > Preferences > Java > Code style > Organize Imports` and remove all the pre-defined groups. This can be done per the whole workspace or per selected project. Google Java Format expects imports to be sorted in alphabetical order and not grouped like the Eclipse default settings.

### IntelliJ

A [Google Java Format IntelliJ plugin](https://plugins.jetbrains.com/plugin/8527) is available from the plugin repository. The plugin will not be enabled by default. To enable it in the current project, go to `File > Settings... > google-java-format Settings` and check `Enable`. To enable it by default in new projects, use `File > Other Settings > Default Settings...`.

When enabled, it will replace the normal _Reformat Code_ action, which can be triggered from the `Code` menu or with the <kbd>Ctrl-Alt-L</kbd> (by default) keyboard shortcut.

## License

This project is licensed under the [MIT license](./LICENSE).
