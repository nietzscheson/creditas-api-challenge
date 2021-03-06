from falcon import testing
from app import application
from model import Base
from database import session, engine

import sqla_yaml_fixtures


class MyAppTestCase(testing.TestCase):
    def setUp(self):
        super(MyAppTestCase, self).setUp()
        self.app = application


class TestMyApp(MyAppTestCase):
    def setUp(self):
        super(TestMyApp, self).setUp()

    def tearDown(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def test_create_lead_auto_aproved(self):
        result = self.simulate_post(
            "/leads",
            body="""{
            "type": "AUTO",
            "name": "Isabella Angulo", 
            "telephone": "123456789",
            "email": "isabella@angulo.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 1",
            "auto": {
              "model": "Ford",
              "price": "200000.00"
            }
          }""",
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "AUTO", "status": "APROVE", "name": "Isabella Angulo", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": {"id": 1, "model": "Ford", "price": 200000.0}}}"""
        self.assertEqual(result.text, response)

    def test_create_lead_auto_rejected(self):
        result = self.simulate_post(
            "/leads",
            body="""{
            "type": "AUTO",
            "name": "Isabella Angulo", 
            "telephone": "123456789",
            "email": "isabella@angulo.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 1",
            "auto": {
              "model": "Ford",
              "price": "600000.00"
            }
          }""",
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "AUTO", "status": "REJECTED", "name": "Isabella Angulo", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": {"id": 1, "model": "Ford", "price": 600000.0}}}"""
        self.assertEqual(result.text, response)

    def test_create_lead_house_aproved(self):
        result = self.simulate_post(
            "/leads",
            body="""{
            "type": "HOUSE",
            "name": "Emmanuel Angulo", 
            "telephone": "123456789",
            "email": "emmanuel@angulo.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 2",
            "house": {
              "address": "CDMX",
              "price": "200000.00"
            }
          }""",
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "HOUSE", "status": "APROVE", "name": "Emmanuel Angulo", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": {"id": 1, "address": "CDMX", "price": 200000.0}}}"""
        self.assertEqual(result.text, response)

    def test_create_lead_house_rejected(self):
        result = self.simulate_post(
            "/leads",
            body="""{
            "type": "HOUSE",
            "name": "Emmanuel Angulo", 
            "telephone": "123456789",
            "email": "emmanuel@angulo.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 2",
            "house": {
              "address": "QROO",
              "price": "800000.00"
            }
          }""",
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "HOUSE", "status": "REJECTED", "name": "Emmanuel Angulo", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": {"id": 1, "address": "QROO", "price": 800000.0}}}"""
        self.assertEqual(result.text, response)

    def test_create_lead_payroll_aproved(self):
        result = self.simulate_post(
            "/leads",
            body="""{
            "type": "PAYROLL",
            "name": "Dulce Agar", 
            "telephone": "123456789",
            "email": "dulce@agar.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 3",
            "payroll": {
              "company": "ABCD inc.",
              "admission_at": "15"
            }
          }""",
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "PAYROLL", "status": "APROVE", "name": "Dulce Agar", "telephone": "123456789", "email": "dulce@agar.com", "rfc": "ABCD1234567890", "address": "Calle 3", "payroll": {"id": 1, "company": "ABCD inc.", "admission_at": "15"}}}"""
        self.assertEqual(result.text, response)

    def test_create_lead_payroll_rejected(self):
        result = self.simulate_post(
            "/leads",
            body="""{
            "type": "PAYROLL",
            "name": "Dulce Agar", 
            "telephone": "123456789",
            "email": "dulce@agar.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 3",
            "payroll": {
              "company": "ABCD inc.",
              "admission_at": "12"
            }
          }""",
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "PAYROLL", "status": "REJECTED", "name": "Dulce Agar", "telephone": "123456789", "email": "dulce@agar.com", "rfc": "ABCD1234567890", "address": "Calle 3", "payroll": {"id": 1, "company": "ABCD inc.", "admission_at": "12"}}}"""
        self.assertEqual(result.text, response)

    def test_get_leads(self):
        leads = """
        - Lead:
          - name: Isabel Angulo
            type: AUTO
            telephone: 123456789
            email: isabela@angulo.com
            rfc: ABCD1234567890
            address: Calle 1
            status: APROVE
          - name: Emmanuel Angulo
            type: HOUSE
            telephone: 123456789
            email: emmanuel@angulo.com
            rfc: ABCD1234567890
            address: Calle 2
            status: REJECTED
          - name: Dulce Agar
            type: PAYROLL
            telephone: 123456789
            email: dulce@agar.com
            rfc: ABCD1234567890
            address: Calle 3
            status: APROVE
        """
        sqla_yaml_fixtures.load(Base, session, leads)

        leads_auto = """
        - LeadAuto:
          - lead_id: 1
            model: Ford
            price: 600000.00
        """
        sqla_yaml_fixtures.load(Base, session, leads_auto)

        leads_house = """
        - LeadHouse:
          - lead_id: 2
            address: CDMX
            price: 200000.00
        """
        sqla_yaml_fixtures.load(Base, session, leads_house)

        leads_payroll = """
        - LeadPayroll:
          - lead_id: 3
            company: ABCD inc.
            admission_at: 15
        """
        sqla_yaml_fixtures.load(Base, session, leads_payroll)
        result = self.simulate_get("/leads")
        response = """{"1": {"name": "Isabel Angulo", "type": "AUTO", "status": "APROVE", "telephone": "123456789", "email": "isabela@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": {"id": 1, "model": "Ford", "price": 600000.0}}, "2": {"name": "Emmanuel Angulo", "type": "HOUSE", "status": "REJECTED", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": {"id": 1, "address": "CDMX", "price": 200000.0}}, "3": {"name": "Dulce Agar", "type": "PAYROLL", "status": "APROVE", "telephone": "123456789", "email": "dulce@agar.com", "rfc": "ABCD1234567890", "address": "Calle 3", "payroll": {"id": 1, "company": "ABCD inc.", "admission_at": "15"}}}"""
        self.assertEqual(result.text, response)
