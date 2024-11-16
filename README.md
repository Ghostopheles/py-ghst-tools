# py-ghst-tools
So, you've found my collection of cadaverous command-line datamining tools, huh? Well, good for you.

## Install

```
pip install git+https://github.com/Ghostopheles/py-ghst-tools.git
```

## Usage
You can view all of the different modules with `ghst --help`.

### Modifier Trees
- `ghst tree view <ModifierTreeID>`: Dumps a ModifierTree to the console in a (hopefully) readable format

### BLP Tools
- `ghst blp view <file_path>`: Opens the specified BLP file in a custom BLP viewer
- `ghst blp convert <file_path> [--format <format>]`: Converts a BLP file to the specified format (default: png).
    - If `file_path` is a directory, it will recursively convert all BLP files found.