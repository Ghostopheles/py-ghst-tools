import typer

from pathlib import Path
from typing import Optional

from ghst.tools.modifier_trees import cmd_dump_tree
from ghst.tools.blp import cmd_view_blp, cmd_convert_blp
from ghst.tools.armadillo import cmd_add_armadillo_key
from ghst.tools.dbc import cmd_fetch_db2s
from ghst.tools.servers import cmd_get_all_realm_statuses, cmd_get_realm_status

app = typer.Typer(name="ghst", add_completion=False, no_args_is_help=True)


# TREE COMMANDS

tree_app = typer.Typer()
app.add_typer(
    tree_app,
    name="tree",
    help="Commands related to ModifierTrees",
    no_args_is_help=True,
)


@tree_app.command(
    name="dump", help="Dump a ModifierTree and it's ancestry to the console"
)
def dump_tree(tree_id: int):
    cmd_dump_tree(tree_id)


# BLP COMMANDS

blp_app = typer.Typer()
app.add_typer(
    blp_app, name="blp", help="BLP file related commands", no_args_is_help=True
)


@blp_app.command(name="view", help="Opens the specified BLP file in a new UI window")
def view_blp(blp_file_path: Path):
    cmd_view_blp(blp_file_path)


@blp_app.command(
    name="convert",
    help="Convert a file or all files in a directory into the specified format",
)
def convert_blp(
    file_path: Path, format: Optional[str] = "png", output_dir: Optional[Path] = None
):
    cmd_convert_blp(file_path, format, output_path=output_dir)


# ARMADILLO COMMANDS

armadillo_app = typer.Typer()
app.add_typer(
    armadillo_app,
    name="armadillo",
    help="Armadillo related commands",
    no_args_is_help=True,
)


@armadillo_app.command(
    name="add", help="Writes an armadillo key to the appropriate key directory"
)
def add_armadillo_key():
    cmd_add_armadillo_key()


# DB2 COMMANDS

db2_app = typer.Typer()
app.add_typer(db2_app, name="db2", help="DB2 commands", no_args_is_help=True)


@db2_app.command(
    name="fetch",
    help="Fetches and saves all DB2s for the specified build to the specified output path",
)
def fetch_db2s(build: str, output_path: Path):
    cmd_fetch_db2s(build, output_path)


# REALM COMMANDS

realm_app = typer.Typer()
app.add_typer(realm_app, name="realms", help="Realm commands", no_args_is_help=True)


@realm_app.command(
    name="status",
    help="Fetches the status of the given realm, or all realms if no realm slug is provided",
)
def get_realm_status(slug: Optional[str] = None):
    if slug is not None:
        cmd_get_realm_status(slug)
    else:
        cmd_get_all_realm_statuses()


def handle_cli():
    app()
