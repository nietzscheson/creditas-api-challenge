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

    def test_create_lead(self):
        result = self.simulate_post("/lead", body=
          """{
            "type": "CAR", 
            "name": "Isabella Angulo", 
            "telephone": "123456789",
            "email": "isabella@angulo.com",
            "rfc": "ABCD1234567890",
            "address": "Calle 1"
          }"""
        )
        print(result.text)
        #self.assertEqual(result.text, data)

