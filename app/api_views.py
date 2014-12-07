from app import api
from app.tni.views import TniUrlListAPI, TniUrlAPI

api.add_resource(TniUrlListAPI, '/api/v1.0/tni', endpoint='tnis')
api.add_resource(TniUrlAPI, '/api/v1.0/tni/<tni_url>', endpoint='tni')
