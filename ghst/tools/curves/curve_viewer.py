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
mpl.rcParams["figure.figsize"] = (5, 5)
mpl.rcParams["lines.linewidth"] = 1
mpl.rcParams["lines.marker"] = "o"
mpl.rcParams["lines.markersize"] = 4
mpl.rcParams["toolbar"] = "none"

LAYOUT_TYPE = "tight"
GRADIENT_GLOW_ALPHA = 0.25
GRADIENT_START = "min"
ANNOTATION_FONTSIZE = 7
ANNOTATION_SNAP_THRESHOLD = 1.0
ANNOTATION_BBOX = dict(
    boxstyle="round,pad=0.4",
    facecolor=mpl.rcParams["figure.facecolor"],
    edgecolor="#08F7FE",
    lw=1,
    alpha=0.8,
)
ANNOTATION_ARROWPROPS = dict(arrowstyle="->", color="#FE53BB")
ANNOTATION_OFFSET_MARGIN = 25
ANNOTATION_OFFSET_AMOUNT = 10


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
    fig, ax = plt.subplots(layout=LAYOUT_TYPE)
    index_to_id = {}
    points = []
    for i, point in enumerate(curve.Points):
        index_to_id[i] = point.ID
        points.append((point.Pos_0, point.Pos_1))

    x_old, y_old = zip(*points)

    x = np.linspace(min(x_old), max(x_old), len(points))
    y = np.interp(x, x_old, y_old)

    ax.plot(x, y, "-", marker="o")

    title = title_override if title_override is not None else "Unknown"
    title += f" (id={curveID})"
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

        ax.set_autoscale_on(False)

        def find_nearest_point(x_mouse, y_mouse):
            distances = np.hypot(x - x_mouse, y - y_mouse)
            index = np.argmin(distances)
            return index, distances[index]

        def calculate_xy_tooltip_offset(x_pos, y_pos):
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()

            margin = ANNOTATION_OFFSET_MARGIN
            offset_amount = ANNOTATION_OFFSET_AMOUNT
            offset_x, offset_y = 15, 15

            if x_pos + margin > xlim[1]:
                offset_x = -(
                    margin + offset_amount
                )  # move left if too close to the right
            elif x_pos - margin < xlim[0]:
                offset_x = margin + offset_amount  # move right if too close to the left

            if y_pos + margin > ylim[1]:
                offset_y = -(
                    margin + offset_amount
                )  # move down if too close to the top
            elif y_pos - margin < ylim[0]:
                offset_y = margin + offset_amount  # move up if too close to the bottom

            return offset_x, offset_y

        hover_annotation = ax.annotate(
            "",
            xy=(0, 0),
            xytext=(15, 15),
            textcoords="offset points",
            bbox=ANNOTATION_BBOX,
            arrowprops=ANNOTATION_ARROWPROPS,
            annotation_clip=False,
            fontsize=ANNOTATION_FONTSIZE,
        )
        hover_annotation.set_visible(False)

        def on_mouse_move(event):
            if event.inaxes != ax:
                hover_annotation.set_visible(False)
                fig.canvas.draw_idle()
                return

            x_mouse, y_mouse = event.xdata, event.ydata
            index, distance = find_nearest_point(x_mouse, y_mouse)

            if distance < ANNOTATION_SNAP_THRESHOLD:
                x_point = x[index]
                y_point = y[index]
                hover_annotation.xy = (x_point, y_point)
                hover_annotation.set_text(
                    f"ID: {index_to_id[index]}\nX: {x_point:.2f}\nY: {y_point:.2f}"
                )

                x_offset, y_offset = calculate_xy_tooltip_offset(x_point, y_point)
                hover_annotation.set_position((x_offset, y_offset))
                hover_annotation.set_visible(True)
            else:
                hover_annotation.set_visible(False)

            fig.canvas.draw_idle()

        fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)
        fig.canvas.manager.set_window_title(f"Curve: {title}")

        plt.show()
