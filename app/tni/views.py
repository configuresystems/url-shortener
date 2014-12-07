from app import app
from flask import abort, redirect
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime


# This is our sample dataset
tni_data = [
        {
            'id': 1,
            'tni_url': 'cs',
            'actual_url': 'http://configure.systems/',
            'created': datetime.datetime.now()
            },
        {
            'id': 2,
            'tni_url': 'goog',
            'actual_url': 'http://google.com/',
            'created': datetime.datetime.now()
            }
        ]

# This is how our data will be returned to us
tni_fields = {
        'tni_url': fields.String,
        'actual_url': fields.String,
        'created':fields.DateTime,
        'uri': fields.Url('tni'),
        }

class TniUrlListAPI(Resource):
    """
    This object handles the creation of new tiny url records and list all
    records
    """
    def __init__(self):
        """
        Set up the fields that can be passed as optional or required via
        a JSON request
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
                'actual_url',
                type=str,
                required=True,
                help='No target URL provided',
                location='json'
                )
        self.reqparse.add_argument(
                'tni_url',
                type=str,
                location='json'
                )
        super(TniUrlListAPI, self).__init__()

    def get(self):
        """
        Return a list of all shortened URLs
        """
        return { 'tni_urls': map(lambda t: marshal(t, tni_fields), tni_data) }

    def post(self):
        """
        Add new object
        """
        pass

class TniUrlAPI(Resource):
    """
    This object deals with setting the 'uri' field in our tni_fields dict,
    selecting a single data object, updating the object, and deleting
    the object
    """
    def __init__(self):
        """
        determines what variables can be passed to the request
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
                'tni_url',
                type=str,
                location='json'
                )
        self.reqparse.add_argument(
                'actual_url',
                type=str,
                location='json'
                )
        super(TniUrlAPI, self).__init__()

    def get(self, tni_url):
        """
        get specific tni_url object
        """
        tni = filter(lambda t: t['tni_url'] == tni_url, tni_data)
        if len(tni) == 0:
            abort(404)
        return { 'tni': marshal(tni[0], tni_fields) }

    def put(self, tni_url):
        """
        Update specific values of an object
        """
        pass

    def delete(self, tni_url):
        """
        delete object
        """
        pass

from .controller import APIMixins
class TniUrlWEB():
    """
    tni.link web views
    """
    @app.route('/<tni_url>', methods=['GET'])
    def tni_route(tni_url):
        """
        redirects the short link to the actual link
        """
        from app.tni.controller import APIMixins
        api_mixins = APIMixins(tni_url=tni_url)
        url = api_mixins.getField(field='actual_url')
        return redirect(url, code=302)
