import falcon
import falcon_sqla

from resource import (
    LeadResource,
)
from database import init_session, engine

init_session()

manager = falcon_sqla.Manager(engine)

app = application = falcon.App(middleware=[manager.middleware])

app.add_route("/leads", LeadResource())
