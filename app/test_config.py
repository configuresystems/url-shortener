from flask.ext.testing import TestCase
from flask import url_for
from app import app, api
from app.hello_world.api_views import messages
import json

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfiguration')
        return app

    def setUp(self):
        with self.client:
            response = self.client.post(
                    url_for('messages'),
                    headers={"Content-Type":"application/json"},
                    data=json.dumps({"message":"Tests are just so fun doe!"})
                    )

    def tearDown(self):
        pass
