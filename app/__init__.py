from flask import Flask
from flask.ext.restful import Api

# instantiate Flask
app = Flask(__name__)
# Set configuration constants
app.config.from_object('config.DebugConfiguration')

# instantiate our API
api = Api(app)

# instantiate our api_views and our web_views
from app import api_views, web_views
