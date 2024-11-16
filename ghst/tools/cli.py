import typer

from pathlib import Path
from typing import Optional

from ghst.tools.modifier_trees import cmd_dump_tree
from ghst.tools.blp import cmd_view_blp, cmd_convert_blp

app = typer.Typer(name="ghst", add_completion=False)


# TREE COMMANDS

tree_app = typer.Typer()
app.add_typer(tree_app, name="tree", help="Commands related to ModifierTrees")


@tree_app.command(
    name="dump", help="Dump a ModifierTree and it's ancestry to the console"
)
def dump_tree(tree_id: int):
    cmd_dump_tree(tree_id)


# BLP COMMANDS

blp_app = typer.Typer()
app.add_typer(blp_app, name="blp", help="BLP file related commands")


@blp_app.command(name="view", help="Opens the specified BLP file in a new UI window")
def view_blp(blp_file_path: Path):
    cmd_view_blp(blp_file_path)


@blp_app.command(
    name="convert",
    help="Convert a file or all files in a directory into the specified format",
)
def convert_blp(file_path: Path, format: Optional[str] = "png"):
    cmd_convert_blp(file_path, format)


def handle_cli():
    app()
