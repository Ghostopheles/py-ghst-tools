import customtkinter as ctk

from PIL import Image
from pathlib import Path

from ghst.tools.shared import exit_with, ASSET_DIR

ICON_PATH = ASSET_DIR.joinpath("gtemp.ico")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

IMAGE_SIZE_PAD = 0.1


class App(ctk.CTk):
    def __init__(self, filename: Path):
        super().__init__()

        self.title(f"BLP Viewer: {filename.name}")

        img = Image.open(
            filename,
            formats=["BLP"],
        )
        image = ctk.CTkImage(img, size=(img.width, img.height))

        xpad = img.width * IMAGE_SIZE_PAD
        ypad = img.height * IMAGE_SIZE_PAD
        label = ctk.CTkLabel(
            self,
            corner_radius=0,
            image=image,
            text="",
        )
        label.pack(anchor="center", expand=True, padx=xpad, pady=ypad)

        geo_width = img.width + (img.width * IMAGE_SIZE_PAD)
        geo_height = img.height + (img.height * IMAGE_SIZE_PAD)
        self.geometry(f"{geo_width}x{geo_height}")

        if ICON_PATH.exists():
            self.wm_iconbitmap(ICON_PATH)


def cmd_view_blp(filename: Path):
    if not filename.exists():
        exit_with(1, "The specified BLP file does not exist")

    app = App(filename)
    app.mainloop()
