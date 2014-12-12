from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))

class BaseConfiguration(object):
    """
    Declaring our default configuration values,
    this is our base object for configuration
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'phee-F1#ph0$fum'

    """
    Set desired hostname or IP address to allow
    us access to the application
    """
    WEB_HOST = 'tni.link'
    WEB_PORT = "5000"
    API_HOST = 'tni.link'
    API_PORT = "5000"

class DebugConfiguration(BaseConfiguration):
    """
    Tailored configuration for debugging
    """
    DEBUG = True

class TestConfiguration(BaseConfiguration):
    """
    Tailored configuration for our running our
    tests
    """
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False

