import os

from pathlib import Path
from typing import Optional
from rich.prompt import Prompt, Confirm

from ghst.tools.shared import exit_with, console


def cmd_add_armadillo_key(
    key_name: Optional[str] = None,
    key_value: Optional[str] = None,
    checksum: Optional[str] = None,
):
    key_dir = Path(os.getenv("APPDATA"), "Battle.net", "Armadillo")
    if not key_dir.exists():
        key_dir.mkdir()

    if key_name is None:
        key_name = Prompt.ask("Key name")
    if key_value is None:
        key_value = Prompt.ask("Key value")
    if checksum is None:
        checksum = Prompt.ask("Checksum")

    key_path = Path(key_dir, f"{key_name}.ak")
    if key_path.exists():
        response = Confirm.ask(
            f"Key {key_name} already exists. Do you want to overwrite it?"
        )
        if not response:
            exit_with(1, "User cancelled operation.")

    with open(key_path, "wb") as keyfile:
        key_bytes = bytes.fromhex(key_value.replace(" ", ""))
        keyfile.write(key_bytes)

        checksum_bytes = bytes.fromhex(checksum.replace(" ", ""))
        keyfile.write(checksum_bytes)

    console.print(
        f"Armadillo key [bright_green]{key_name}[/bright_green] written successfully."
    )
