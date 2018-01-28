# Extenda pre-commit hooks

This repository contains pre-commit hooks by Extenda.

See also: http://pre-commit.com for general usage instructions.

## Usage with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/extenda/pre-commit-hooks
    sha: v1.0 # Use the ref you want to point at
    hooks:
    -   id: eclipse-formatter
```

## Available hooks

* `eclipse-formatter` - Runs Eclipse Java formatter on all staged `java` source files. The following arguments are available:
  * `--source` - set the Java compiler source version (default `1.8`)
  * `--target` - set the Java compiler target version (default `1.8`)
