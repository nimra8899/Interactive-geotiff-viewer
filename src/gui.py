import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

class GeoApp:
    def __init__(self, root, geotiff):
        self.root = root
        self.geotiff = geotiff

        self.root.title("GeoTIFF Viewer")

        # Load image
        array = self.geotiff.read_image()

        if len(array.shape) == 3:
            array = np.transpose(array, (1, 2, 0))

        array = (array / array.max() * 255).astype(np.uint8)
        self.original_image = Image.fromarray(array)

        self.scale = 1.0
        self.image = self.original_image
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        # Labels
        self.xy_label = tk.Label(root, text="X,Y: ")
        self.xy_label.pack()

        self.geo_label = tk.Label(root, text="Lat,Lon: ")
        self.geo_label.pack()

        # Input
        self.lat_entry = tk.Entry(root)
        self.lat_entry.pack()

        self.lon_entry = tk.Entry(root)
        self.lon_entry.pack()

        self.mark_btn = tk.Button(root, text="Mark", command=self.mark_location)
        self.mark_btn.pack()

        # Bindings
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan)

        self.pan_start = None

    # -----------------------------
    # MOUSE TRACKING (Task B)
    # -----------------------------
    def mouse_move(self, event):
        x = int(event.x / self.scale)
        y = int(event.y / self.scale)

        lat, lon = self.geotiff.pixel_to_geo(x, y)

        self.xy_label.config(text=f"X,Y: {x}, {y}")
        self.geo_label.config(text=f"Lat,Lon: {lat:.4f}, {lon:.4f}")

    # -----------------------------
    # MARK LOCATION (Task C)
    # -----------------------------
    def mark_location(self):
        try:
            lat = float(self.lat_entry.get())
            lon = float(self.lon_entry.get())

            x, y = self.geotiff.geo_to_pixel(lat, lon)

            x = x * self.scale
            y = y * self.scale

            self.canvas.create_line(x-5, y, x+5, y, fill="red", width=2)
            self.canvas.create_line(x, y-5, x, y+5, fill="red", width=2)

        except:
            print("Invalid input")

    # -----------------------------
    # ZOOM (Task D)
    # -----------------------------
    def zoom(self, event):
        if event.delta > 0:
            self.scale *= 1.1
        else:
            self.scale /= 1.1

        new_size = (
            int(self.original_image.width * self.scale),
            int(self.original_image.height * self.scale)
        )

        self.image = self.original_image.resize(new_size)
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.canvas.itemconfig(self.image_id, image=self.tk_image)

    # -----------------------------
    # PAN (Task D)
    # -----------------------------
    def start_pan(self, event):
        self.pan_start = (event.x, event.y)

    def pan(self, event):
        dx = event.x - self.pan_start[0]
        dy = event.y - self.pan_start[1]

        self.canvas.move(self.image_id, dx, dy)
        self.pan_start = (event.x, event.y)