"""
TEMPLATE: https://github.com/sharksmhi/microservice_template

Examples:
    get:
        http://localhost:5000/positions
    post:
        http://localhost:5000/positions/58&20&-
        http://localhost:5000/positions/58&20&NAMN
"""
import connexion
from water_bodies import PositionRegistry, PositionDoesNotExist

registry = PositionRegistry()


def get_area_example(*args, **kwargs):
    return registry.get_example()


def get_water_body(latitude=None, longitude=None, key=None, **kwargs):
    if key and key != '-':
        return registry.get_water_body_key(latitude, longitude, key)
    else:
        return registry.get_water_body(latitude, longitude)


app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={'swagger_url': '/'},
)
app.add_api('openapi.yaml')
app.run(port=5000)
