from pathlib import Path
from typing import Optional
from rich.console import Console

console = Console()

ASSET_DIR = Path(__file__).parent.with_stem("assets")


def exit_with(code: int, message: Optional[str] = None, style: Optional[str] = None):
    if message is not None:
        if style is None:
            style = "red" if code > 0 else ""
        console.print(message, style=style)

    exit(code)
