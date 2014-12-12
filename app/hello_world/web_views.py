from app import app
from flask import Blueprint, render_template
import requests


web = Blueprint('messages', __name__)

class HelloWorldWeb(object):
    @web.route('/hello/world', methods=['GET'])
    def web_index():
        url = "http://{0}:{1}/api/{2}/1".format(
                app.config['API_HOST'],
                app.config['API_PORT'],
                'message'
                )
        headers = { "Content-Type": "application/json" }
        request = requests.get(
                url,
                headers=headers,
                ).json()
        return render_template(
                "index.html",
                title="Tiny Link - Part 1 - Hello World",
                message=request['message']
                )

    @web.route('/messages', methods=['GET'])
    @web.route('/messages/list', methods=['GET'])
    def web_list():
        url = "http://{0}:{1}/api/{2}".format(
                app.config['API_HOST'],
                app.config['API_PORT'],
                'messages'
                )
        headers = { "Content-Type": "application/json" }
        request = requests.get(
                url,
                headers=headers,
                ).json()
        return render_template(
                "list.html",
                title="Tiny Link - Part 1 - Hello World",
                messages=request
                )
