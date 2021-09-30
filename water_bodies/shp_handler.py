"""
Created on 2021-03-25 20:33
@author: johannes
"""
import os
import geopandas as gp
from shapely.geometry import Point


RESOURCES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data', 'resources'
)


class SHARKGeoDataFrame(gp.GeoDataFrame):
    """Description."""

    @property
    def _constructor(self):
        """Description."""
        return SHARKGeoDataFrame

    def to_geojson(self, **kwargs):
        """Return a python feature collection (i.e. the geointerface)
        representation of the GeoDataFrame."""
        geo = {
            "type": "FeatureCollection",
            "features": list(self.iterfeatures(**kwargs)),
        }

        if kwargs.get("show_bbox", False):
            geo["bbox"] = tuple(self.total_bounds)

        return geo


class ShapeHandler:
    """Handler for shapefile.

    Using basin from the shapefile Havsomr_SVAR_2016_3b_cp1252
    in order to find area location information for a certain position.
    """

    def __init__(self):
        """Initialize."""
        shapes = gp.read_file(os.path.join(RESOURCES, 'Havsomr_SVAR_2016_3b_cp1252.shp'))
        self.shapes = SHARKGeoDataFrame(shapes)

    def get_example(self, obj_id=48):
        """Return example."""
        # return self.shapes[self.shapes['OBJECTID'] == obj_id].to_geojson()
        return self.shapes[self.shapes['OBJECTID'] == obj_id]._to_geo()

    def find_area_for_point(self, lat, lon):
        """Return area information about the given location.

        Includes polygon.
        """
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            # return self.shapes[boolean].to_geojson()
            return self.shapes[boolean]._to_geo()

    def get_key_value_for_point(self, lat, lon, key):
        """Return area information about the given location and attribute."""
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return {key: self.shapes.loc[boolean, key].values[0]}

    def get_position_info(self, latitude=None, longitude=None, attribute=None):
        """Return information based on arguments."""
        if not attribute and (latitude and longitude):
            return self.find_area_for_point(latitude, longitude)
        elif all((latitude, longitude, attribute)):
            return self.get_key_value_for_point(latitude, longitude, attribute)
        elif all(v is None for v in (latitude, longitude, attribute)):
            return self.get_example()
        else:
            return (
                'Missing parameters, got latitude={}; longitude={}; attribute={}'.format(
                    latitude,
                    longitude,
                    attribute
                ),
                404
            )
