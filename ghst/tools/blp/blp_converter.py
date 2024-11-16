import os
import random

from PIL import Image
from pathlib import Path
from typing import Optional, Union
from rich.prompt import Confirm, Prompt
from rich.table import Column
from rich.progress import (
    Progress,
    TextColumn,
    SpinnerColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
)
from concurrent.futures import ThreadPoolExecutor, wait

from ghst.tools.shared import exit_with, console

SPINNERS = [
    "pong",
    "moon",
    "runner",
    "dots12",
]


def get_all_blp_files(path: Path) -> list[Path]:
    all_blp_files = []
    for root, _, files in os.walk(path, topdown=True):
        for file in files:
            if file.lower().endswith(".blp"):
                full_path = os.path.join(root, file)
                all_blp_files.append(Path(full_path))

    return all_blp_files


def _convert_blp(
    file_path: Path,
    format: str,
    progress: Optional[Progress] = None,
    root_task=None,
    display_name: Optional[str] = None,
    exist_ok: Optional[bool] = True,
    output_path: Optional[Path] = None,
):
    if output_path is not None:
        name = Path(display_name)
        new_path = output_path.joinpath(name).with_suffix(f".{format}")
        new_parent_path = Path(new_path.parent)
        if not new_parent_path.exists():
            new_parent_path.mkdir()
    else:
        new_path = file_path.with_suffix(f".{format}")
    if new_path.exists() and not exist_ok:
        response = Confirm.ask(
            f'Destination file "{new_path.name}" already exists. Continue?'
        )
        if not response:
            exit_with(1, "User cancelled conversion operation.")

    do_progress = progress is not None

    if do_progress:
        progress.update(root_task, advance=0.5, filename=display_name)

    img = Image.open(file_path, formats=["BLP"])
    img.save(new_path, format=format)

    if do_progress:
        progress.update(root_task, advance=0.5)


def convert_blp_files(
    file_paths: Union[Path, list[Path]],
    format: str,
    root_path: Optional[Path] = None,
    output_path: Optional[Path] = None,
):
    if isinstance(file_paths, list):  # full directory
        num_files = len(file_paths)
        response = Confirm.ask(f"You are about to convert {num_files} files. Continue?")
        if not response:
            exit_with(1, "User cancelled conversion operation.")

        with Progress(
            SpinnerColumn(spinner_name=random.choice(SPINNERS)),
            TextColumn(
                "{task.description}[cyan]{task.fields[filename]}[/cyan]",
                table_column=Column(ratio=2, no_wrap=True),
            ),
            BarColumn(bar_width=None, table_column=Column(justify="right", ratio=1)),
            TaskProgressColumn(justify="right"),
            TimeRemainingColumn(elapsed_when_finished=True),
            console=console,
            expand=True,
        ) as progress:
            root_task = progress.add_task(
                "Converting: ",
                filename="N/A",
                total=num_files,
            )
            with ThreadPoolExecutor(os.cpu_count()) as pool:
                futures = []
                for file in file_paths:
                    display_name = (
                        file.relative_to(root_path)
                        if root_path is not None
                        else file.name
                    )
                    futures.append(
                        pool.submit(
                            _convert_blp,
                            file,
                            format,
                            progress=progress,
                            root_task=root_task,
                            display_name=display_name,
                            output_path=output_path,
                        )
                    )

                wait(futures)
    else:  # just one file
        console.print("Converting file...")
        _convert_blp(file_paths, format, exist_ok=False)

    console.print("Conversion complete", style="u bright_green")


def cmd_convert_blp(
    path: Path, format: Optional[str] = None, output_path: Optional[Path] = None
):
    if not path.exists():
        exit_with(1, "The specified path does not exist.")

    if format is None:
        format = Prompt.ask("Specify a format for the converted files", default="png")

    if path.is_dir():
        all_files = get_all_blp_files(path)
        convert_blp_files(all_files, format, root_path=path, output_path=output_path)
    else:
        convert_blp_files(path, format, output_path=output_path)
