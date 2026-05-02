from osgeo import gdal

class GeoTIFFHandler:
    def __init__(self, filepath):
        self.dataset = gdal.Open(filepath)
        if self.dataset is None:
            raise Exception("Failed to load GeoTIFF")

        self.transform = self.dataset.GetGeoTransform()

    def pixel_to_geo(self, x, y):
        gt = self.transform
        lon = gt[0] + x * gt[1] + y * gt[2]
        lat = gt[3] + x * gt[4] + y * gt[5]
        return lat, lon

    def geo_to_pixel(self, lat, lon):
        gt = self.transform
        x = int((lon - gt[0]) / gt[1])
        y = int((lat - gt[3]) / gt[5])
        return x, y

    def read_image(self):
        band = self.dataset.ReadAsArray()
        return band