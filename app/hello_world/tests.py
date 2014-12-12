from flask import url_for
from app.test_config import BaseTestCase
from app.hello_world import api_views
import json


class HelloWorldTests(BaseTestCase):
    def test_get_all_messages(self):
        with self.client:
            response = self.client.get(url_for('messages'))
            self.assert200(response)

    def test_get_single_message(self):
        with self.client:
            add = self.client.post(
                    url_for('messages'),
                    headers={"Content-Type":"application/json"},
                    data=json.dumps({"message":"Hello World"})
                    )
            response = self.client.get(url_for('message', id=add.json['message']['id']))
            self.assert200(response, "Invalid Request")
            self.assertEqual(
                    "Hello World",
                    response.json['message']['message']
                    )

    def test_post_new_message(self):
        with self.client:
            response = self.client.post(
                    url_for('messages'),
                    headers={"Content-Type":"application/json"},
                    data=json.dumps({"message":"Tests are just so fun doe!"})
                    )
            self.assertStatus(response, 201)
            self.assertEqual("Tests are just so fun doe!", response.json['message']['message'])

    def test_update_message(self):
        with self.client:
            response = self.client.put(
                    url_for('message', id=1),
                    headers={"Content-Type":"application/json"},
                    data=json.dumps({"message":"Message Updated"})
                    )
            self.assert200(response)
            self.assertEqual("Message Updated", response.json['message']['message'])

    def test_delete_message(self):
        with self.client:
            response = self.client.delete(
                    url_for('message', id=1),
                    headers={"Content-Type":"application/json"},
                    )
