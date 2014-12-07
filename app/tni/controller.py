from app.common.controller import APICrud

class APIMixins(APICrud):
    """
    Object for controlling our shorted url dataset
    """
    def __init__(self, tni_url, data=None):
        self.tni_url = tni_url
        self.data = data

    def checkData(self, tni_url=None):
        """
        checks if we have any data, if not, its goes and gets the data
        """
        if not self.data:
            self.getData(tni_url)
        return True

    def getData(self, tni_url=None):
        """
        grabs our single object dataset
        """
        self.data = self.get(endpoint='tni', tni_url=tni_url)
        return self.data

    def getField(self, field, tni_url=None):
        """
        parse dataset to obtain the desired field.  such as for redirection,
        we return the value of actual_url.
        """
        if tni_url:
            self.tni_url = tni_url
        self.checkData(self.tni_url)
        return self.data['tni'][field]
