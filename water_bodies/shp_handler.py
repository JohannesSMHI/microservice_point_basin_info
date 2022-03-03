"""
Created on 2021-03-25 20:33
@author: johannes
"""
from pathlib import Path
import geopandas as gp
from shapely.geometry import Point


RESOURCES = Path(__file__).parent.joinpath('data', 'resources')
ERROR_STRING = 'Missing parameters, got latitude={}; longitude={}; attribute={}'


class SHARKGeoDataFrame(gp.GeoDataFrame):
    """Description."""

    @property
    def _constructor(self):
        """Description."""
        return SHARKGeoDataFrame

    def to_geojson(self, boolean):
        """Return a python feature collection (i.e. the geointerface)
        representation of the GeoDataFrame."""
        return self[boolean]._to_geo()


class ShapeHandler:
    """Handler for shapefile.

    Using basin from the shapefile Havsomr_SVAR_2016_3b_cp1252
    in order to find area location information for a certain position.
    """

    def __init__(self):
        """Initialize."""
        shapes = gp.read_file(RESOURCES.joinpath(
            'Havsomr_SVAR_2016_3b_cp1252.shp')
        )
        self.shapes = SHARKGeoDataFrame(shapes)

    def get_example(self, obj_id=48):
        """Return example."""
        return self.shapes.to_geojson(self.shapes['OBJECTID'] == obj_id)

    def find_area_for_point(self, lat, lon):
        """Return area information about the given location.

        Includes polygon.
        """
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return self.shapes.to_geojson(boolean)
        else:
            return ERROR_STRING.format(lat, lon, ''), 404

    def get_key_value_for_point(self, lat, lon, key):
        """Return area information about the given location and attribute."""
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return {key: self.shapes.loc[boolean, key].values[0]}
        else:
            return ERROR_STRING.format(lat, lon, key), 404

    def get_position_info(self, latitude=None, longitude=None, attribute=None):
        """Return information based on arguments."""
        if not attribute and (latitude and longitude):
            return self.find_area_for_point(latitude, longitude)
        elif all((latitude, longitude, attribute)):
            return self.get_key_value_for_point(latitude, longitude, attribute)
        elif all(v is None for v in (latitude, longitude, attribute)):
            return self.get_example()
        else:
            return ERROR_STRING.format(latitude, longitude, attribute), 404
