import os
from water_bodies.shp_handler import ShapeHandler


RESOURCES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data', 'resources'
)


class PositionRegistry:
    def __init__(self):
        self.sh = ShapeHandler(
            path=os.path.join(RESOURCES, 'Havsomr_SVAR_2016_3b_cp1252.shp')
        )

    def get_water_body(self, lat, lon):
        try:
            return self.sh.find_area_for_point(lat, lon)
        except:
            raise PositionDoesNotExist()

    def get_water_body_key(self, lat, lon, key):
        try:
            return self.sh.get_key_value_for_point(lat, lon, key)
        except:
            raise PositionDoesNotExist()

    def get_example(self):
        return self.sh.get_example()


class PositionDoesNotExist(Exception):
    pass
