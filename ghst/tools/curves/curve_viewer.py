import httpx

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from pathlib import Path
from typing import Optional
from dataclasses import dataclass

from ghst.tools.shared import console

WAGO_CSV_URL = "https://wago.tools/db2/{db2name}/csv"
BUILD_FORMAT = "?build={build}"

LINE_WIDTH = 0.5
FIGURE_SIZE = (8, 5)
POINT_MARKER_SIZE = 1.5
GRADIENT_GLOW_ALPHA = 0.25
GRADIENT_START = "min"

USE_CYBERPUNK = False
try:
    import mplcyberpunk

    mpl.style.use("cyberpunk")
    USE_CYBERPUNK = True
except ImportError:
    pass

mpl.rcParams["font.size"] = 10
mpl.rcParams["figure.titlesize"] = 20
mpl.rcParams["figure.dpi"] = 150


@dataclass
class CurvePoint:
    Pos_0: float
    Pos_1: float
    PosPreSquish_0: float
    PosPreSquish_1: float
    ID: int
    CurveID: int
    OrderIndex: int


@dataclass
class Curve:
    ID: int
    Type: int
    Flags: int
    Points: list[CurvePoint]


def convert_curve_point(curve_point_data: list[str]):
    converted = []
    converted.append(float(curve_point_data[0]))
    converted.append(float(curve_point_data[1]))
    converted.append(float(curve_point_data[2]))
    converted.append(float(curve_point_data[3]))
    converted.append(int(curve_point_data[4]))
    converted.append(int(curve_point_data[5]))
    converted.append(int(curve_point_data[6]))

    return converted


def stream(url: str):
    with httpx.Client(http2=True).stream("GET", url, follow_redirects=True) as stream:
        for line in stream.iter_lines():
            yield line


# fetch both the Curve and CurvePoint DB2s
def fetch_db2_data(curveID: int, build: Optional[str] = None) -> Optional[Curve]:
    curveID = str(curveID)
    curve_url = WAGO_CSV_URL.format(db2name="Curve")
    curvepoints_url = WAGO_CSV_URL.format(db2name="CurvePoint")

    if build is not None:
        build_query = BUILD_FORMAT.format(build=build)
        curve_url += build_query
        curvepoints_url += build_query

    curve_data = None

    console.print("Streaming Curve.db2 from [blue]wago.tools[/blue]...")
    for line in stream(curve_url):
        line_split = line.split(",")
        if line_split[0] == curveID:
            curve_data = [int(value) for value in line_split]
            break

    if curve_data is None:
        console.print(f"[bold red]Curve with ID={curveID} not found.[/bold red]")
        return None

    curve_points = []

    console.print("Streaming CurvePoint.db2 from [blue]wago.tools[/blue]...")
    for line in stream(curvepoints_url):
        line_split = line.split(",")
        if line_split[5] == curveID:
            curve_point_data = convert_curve_point(line_split)
            curve_points.append(CurvePoint(*curve_point_data))

    return Curve(*curve_data, curve_points)


def cmd_view_curve(
    curveID: int,
    title_override: Optional[str] = None,
    export_path: Optional[Path] = None,
    no_show: Optional[bool] = False,
    build: Optional[str] = None,
):
    curve = fetch_db2_data(curveID, build)
    if curve is None or len(curve.Points) == 0:
        console.print(f"[bold red]Failed to render curve.[/bold red]")
        return None

    # plotting and scheming
    fig, ax = plt.subplots(layout="constrained", figsize=FIGURE_SIZE)
    points = [(point.Pos_0, point.Pos_1) for point in curve.Points]
    x, y = zip(*points)

    x_new = np.linspace(min(x), max(x), 100)
    y_new = np.interp(x_new, x, y)

    ax.plot(
        x_new,
        y_new,
        "-",
        linewidth=LINE_WIDTH,
        marker="o",
        markersize=POINT_MARKER_SIZE,
    )

    title = title_override if title_override is not None else f"Curve {curveID}"
    ax.set_title(title)

    if USE_CYBERPUNK:
        mplcyberpunk.make_lines_glow(ax)
        mplcyberpunk.add_gradient_fill(
            ax, alpha_gradientglow=GRADIENT_GLOW_ALPHA, gradient_start=GRADIENT_START
        )

    if export_path is not None:
        format = mpl.rcParams["savefig.format"]
        full_export_path = export_path / f"Curve_{curveID}.{format}"
        plt.savefig(full_export_path, bbox_inches="tight")
        console.print(
            f"Successfully saved figure for curve {curveID} to '{full_export_path}'"
        )

    if not no_show:
        plt.show()
