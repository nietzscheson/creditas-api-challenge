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

    def test_create_lead_auto_aprove(self):
        result = self.simulate_post("/lead", body=
          """{
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
          }"""
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "AUTO", "status": "APROVE", "name": "Isabella Angulo", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": {"id": 1, "model": "Ford", "price": 200000.0}}}"""
        self.assertEqual(result.text, response)
        
    def test_create_lead_auto_rejected(self):
        result = self.simulate_post("/lead", body=
          """{
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
          }"""
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "AUTO", "status": "REJECTED", "name": "Isabella Angulo", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": {"id": 1, "model": "Ford", "price": 600000.0}}}"""
        self.assertEqual(result.text, response)
        
    def test_create_lead_house_aprove(self):
        result = self.simulate_post("/lead", body=
          """{
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
          }"""
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "HOUSE", "status": "APROVE", "name": "Emmanuel Angulo", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": {"id": 1, "address": "CDMX", "price": 200000.0}}}"""
        self.assertEqual(result.text, response)
        
    def test_create_lead_house_rejected(self):
        result = self.simulate_post("/lead", body=
          """{
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
          }"""
        )
        response = """{"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "HOUSE", "status": "REJECTED", "name": "Emmanuel Angulo", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": {"id": 1, "address": "QROO", "price": 800000.0}}}"""
        self.assertEqual(result.text, response)