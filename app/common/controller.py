from config import BaseConfiguration
import requests
import json

class APICrud():
    """
    Our API CRUD.  We will use this object to Create, Update, and delete
    our data via the API
    """
    def __init__(self):
        pass

    def get(self, endpoint, tni_url):
        """
        Get a specific object
        """
        url = "http://{0}:{1}/api/v1.0/{2}/{3}".format(
                BaseConfiguration.HOST,
                BaseConfiguration.PORT,
                endpoint,
                tni_url
                )
        headers = {'Content-Type': 'application/json'}
        request = requests.get(
                url,
                headers=headers
                ).json()
        return request
