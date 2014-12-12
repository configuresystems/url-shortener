from flask import Flask
from flask.ext.restful import Api
#from .hello_world.web_views import hello_world_web

app = Flask(__name__)
app.debug = True
app.config.from_object('config.DebugConfiguration')

# Instantiate the API
api = Api(app)

from app.hello_world.api_views import HelloWorldApi, HelloWorldListApi
api.add_resource(HelloWorldListApi, '/api/messages', endpoint='messages')
api.add_resource(HelloWorldApi, '/api/messages/<int:id>', endpoint='message')

from app.hello_world.web_views import web
app.register_blueprint(web, url_prefix='/web')
