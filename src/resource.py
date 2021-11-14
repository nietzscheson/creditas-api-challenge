import json

import falcon
from sqlalchemy import func, desc, extract, and_
from model import Lead, LeadType, LeadAuto, LeadStatus

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
        
        ## Status for LeadAuto
        if lead.type == LeadType.AUTO.value:
            lead.status = LeadStatus.REJECTED.value
            auto = data["auto"]
            
            if 200000 <= float(auto["price"]) <= 500000:
                lead.status = LeadStatus.APROVE.value
                
        session.add(lead)
        session.flush()
        
        try:
            
            if lead.type == LeadType.AUTO.value:
                lead_auto = LeadAuto()
                lead_auto.lead_id = lead.id
                auto = data["auto"]
                lead_auto.price = auto["price"]
                lead_auto.model = auto["model"]
                
                session.add(lead_auto)
                session.flush()
                
            session.commit()
            
            data = lead.as_dict()
            if lead.type.value == LeadType.AUTO.value:
                data["auto"] = lead_auto.as_dict()
                
            resp.media = {"message": f"The Lead {lead.id} record has been created!", 'data': data}
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.text = f"Error: {e}"
            resp.status = falcon.HTTP_400