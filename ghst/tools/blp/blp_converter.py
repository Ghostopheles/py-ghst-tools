import os
import subprocess

from PIL import Image
from pathlib import Path
from typing import Optional, Union
from rich.prompt import Confirm, Prompt
from concurrent.futures import ThreadPoolExecutor, wait

from ghst.tools.shared import exit_with, console


def get_all_blp_files(path: Path) -> list[Path]:
    all_blp_files = []
    for root, _, files in os.walk(path, topdown=True):
        for file in files:
            if file.lower().endswith(".blp"):
                full_path = os.path.join(root, file)
                all_blp_files.append(Path(full_path))

    return all_blp_files


def _convert_blp(file_path: Path, format: str, exist_ok: Optional[bool] = True):
    img = Image.open(file_path, formats=["BLP"])
    new_path = file_path.with_suffix(f".{format}")
    if new_path.exists() and not exist_ok:
        response = Confirm.ask(
            f'Destination file "{new_path.name}" already exists. Continue?'
        )
        if not response:
            exit_with(1, "User cancelled conversion operation.")

    img.save(new_path, format=format)


def convert_blp_files(file_paths: Union[Path, list[Path]], format: str):
    if isinstance(file_paths, list):  # full directory
        num_files = len(file_paths)
        response = Confirm.ask(f"You are about to convert {num_files} files. Continue?")
        if not response:
            exit_with(1, "User cancelled conversion operation.")

        with ThreadPoolExecutor(os.cpu_count()) as pool:
            futures = []
            for file in file_paths:
                futures.append(pool.submit(_convert_blp, file, format))

            wait(futures)
    else:  # just one file
        console.print("Converting file...")
        _convert_blp(file_paths, format, exist_ok=False)

    console.print("Conversion complete", style="u bright_green")


def cmd_convert_blp(path: Path, format: Optional[str] = None):
    if not path.exists():
        exit_with(1, "The specified path does not exist.")

    if format is None:
        format = Prompt.ask("Specify a format for the converted files", default="png")

    if path.is_dir():
        all_files = get_all_blp_files(path)
        convert_blp_files(all_files, format)
    else:
        convert_blp_files(path, format)
