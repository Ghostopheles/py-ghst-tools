# py-ghst-tools
So, you've found my collection of cadaverous command-line datamining tools, huh? Well, good for you, and good luck.

## Install

```
pip install git+https://github.com/Ghostopheles/py-ghst-tools.git
```

## Usage
You can view all of the different modules with `ghst --help`.

### Modifier Trees
- `ghst tree dump <ModifierTreeID>`: Dumps a ModifierTree to the console in a (hopefully) readable format

### BLP Tools
- `ghst blp view <file_path>`: Opens the specified BLP file in a custom BLP viewer
- `ghst blp convert <file_path> [--format <format>]`: Converts a BLP file to the specified format (default: png)
    - If `file_path` is a directory, it will recursively convert all BLP files found

### Armadillo
- `ghst armadillo add`: Interactively add an armadillo key to the appropriate location for it to be recognized by the Battle.net client

### DB2s
- `ghst db2 fetch <build> <output_path>`: Downloads all DB2s for the `<build>` from wago.tools and saves them to `<output_path>`

### Curves
- `ghst curves view <curveID> [--title <title> --export-path <path> --build <build> --no-show]`: Plots and shows a graph representing the specified curve.