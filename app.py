"""
TEMPLATE: https://github.com/sharksmhi/microservice_template

Examples:
    get:
        http://localhost:5000/positions
    post:
        http://localhost:5000/positions?latitude=58&longitude=20
        http://localhost:5000/positions?latitude=58&longitude=20&attribute=NAMN
        # http://localhost:5000/positions?58&20&-
        # http://localhost:5000/positions?58&20&NAMN
"""
import connexion
from water_bodies import ShapeHandler

handler = ShapeHandler()


def get_info(*args, latitude=None, longitude=None, attribute=None, **kwargs):
    """Get function."""
    return handler.get_position_info(
        latitude=latitude,
        longitude=longitude,
        attribute=attribute
    )


app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={'swagger_url': '/'},
)
app.add_api('openapi.yaml')
app.run(port=5000)
