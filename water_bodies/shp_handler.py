"""
Created on 2021-03-25 20:33
@author: johannes
"""
import geopandas as gp
from shapely.geometry import Point


class ShapeHandler:
    def __init__(self, path=None):
        self.shapes = gp.read_file(path) if path else gp.GeoDataFrame()

    def find_area_for_point(self, lat, lon):
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return self.shapes[boolean]._to_geo()

    def get_key_value_for_point(self, lat, lon, key):
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return {key: self.shapes.loc[boolean, key].values[0]}

    def get_example(self, obj_id=48):
        return self.shapes[self.shapes['OBJECTID'] == obj_id]._to_geo()


if __name__ == '__main__':
    sh = ShapeHandler(path=r'data\resources\Havsomr_SVAR_2016_3b_cp1252.shp')
    # geo = sh.shapes.iloc[:2]._to_geo()
    geo = sh.shapes[sh.shapes['OBJECTID'] == 48]._to_geo()
