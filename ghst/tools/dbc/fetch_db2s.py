import os
import httpx
import concurrent.futures

from pathlib import Path
from typing import Optional

from ghst.tools.shared import console

g_currentBuild = None

LISTFILE_URL = "https://github.com/wowdev/wow-listfile/releases/latest/download/community-listfile.csv"
WAGO_URL = "https://wago.tools/api/casc/{fdid}?version={build}"


def fetch_listfile():
    console.print("Streaming listfile...")
    with httpx.Client(http2=True).stream(
        "GET", LISTFILE_URL, follow_redirects=True
    ) as stream:
        for line in stream.iter_lines():
            if line and line.endswith("db2"):
                fdid, name = line.split(";", maxsplit=2)
                yield fdid, name


def fetch_and_save_db2(output_path: Path, fdid: int, name: str):
    global g_currentBuild
    if g_currentBuild is None:
        return

    if fdid is None or name is None:
        return

    if not name.endswith("db2"):
        return

    dest_folder = Path(output_path, g_currentBuild)
    os.makedirs(Path(dest_folder, "dbfilesclient"), exist_ok=True)

    filename = name.lower()
    dest = Path(dest_folder, filename)
    console.print(f"Streaming {filename} ({fdid})...")
    with httpx.Client(http2=True).stream(
        "GET", WAGO_URL.format(fdid=fdid, build=g_currentBuild)
    ) as stream:
        with open(dest, "wb") as file:
            for chunk in stream.iter_bytes():
                file.write(chunk)


def cmd_fetch_db2s(build: str, output_path: Path):
    global g_currentBuild
    g_currentBuild = build

    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [
            executor.submit(fetch_and_save_db2, output_path, fdid, name)
            for fdid, name in fetch_listfile()
        ]

    concurrent.futures.wait(futures)

    console.print("Done!")
