import json

import falcon
from sqlalchemy import func, desc, extract, and_
from model import Lead


class LeadResource:
    def on_get(self, req, resp):
        session = req.context["session"]

        resp.text = json.dumps("Hello Lead")
        resp.status = falcon.HTTP_200
        
    def on_post(self, req, resp):
        session = req.context["session"]

        data = req.media
        lead = Lead()

        lead.type = data["type"]
        lead.name = data["name"]
        lead.telephone = data["telephone"]
        lead.email = data["email"]
        lead.rfc = data["rfc"]
        lead.address = data["address"]

        try:
            session.add(lead)
            session.commit()
            print(lead.type)
            # resp.media = {'data': json.loads(lead)}
            resp.media = {"message": f"The Lead {lead.id} record has been created!", 'data': {}}
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.text = f"Error: {e}"
            resp.status = falcon.HTTP_400