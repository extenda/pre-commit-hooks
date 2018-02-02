# Extenda pre-commit hooks

This repository contains pre-commit hooks by Extenda.

See also: http://pre-commit.com for general usage instructions.

## Usage with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: git@github.com:extenda/pre-commit-hooks.git
    sha: v1.0 # Use the ref you want to point at
    hooks:
    -   id: google-java-formatter
```

## Available hooks

* `eclipse-formatter` - Runs Eclipse Java formatter with default formatting rules on all staged `java` source files. The following arguments are available:
  * `--source` - set the Java compiler source version (default `1.8`)
  * `--target` - set the Java compiler target version (default `1.8`)
* `google-java-formatter` - Runs Google's Java formatter on all staged `java` source files.

## Google Java format in your IDE

There's a Google Java Format plugin for both Eclipse and IntelliJ.

The current version used is `1.5`.

### Eclipse

[Download the formatter plugin](https://github.com/google/google-java-format/releases/download/google-java-format-1.5/google-java-format-eclipse-plugin_1.5.0.jar) and drop it into Eclipse's `dropins` folder.

The plugin adds a `google-java-format` formatter implementation that can be configured in `Window > Preferences > Java > Code Style > Formatter > Formatter Implementation`.

You must also change `Window > Preferences > Java > Code style > Organize Imports` and remove all the pre-defined groups. Google Java Format expects imports to be sorted in alphabetical order and not grouped like the Eclipse default settings.

### IntelliJ

A [Google Java Format IntelliJ plugin](https://plugins.jetbrains.com/plugin/8527) is available from the plugin repository. The plugin will not be enabled by default. To enable it in the current project, go to `File > Settings... > google-java-format Settings` and check `Enable`. To enable it by default in new projects, use `File > Other Settings > Default Settings...`.

When enabled, it will replace the normal _Reformat Code_ action, which can be triggered from the `Code` menu or with the `Ctrl-Alt-L` (by default) keyboard shortcut.
