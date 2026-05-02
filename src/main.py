import tkinter as tk
from geo_utils import GeoTIFFHandler
from gui import GeoApp

if __name__ == "__main__":
    file_path = "../data/testGeoTiff.tif"

    geotiff = GeoTIFFHandler(file_path)

    root = tk.Tk()
    app = GeoApp(root, geotiff)

    root.mainloop()