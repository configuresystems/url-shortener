from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))

class BaseConfiguration(object):
    """
    Setting up some constant variables
    """
    DEBUG = False
    TESTING = False
    HOST = 'tni.link'
    PORT = "5000"

class DebugConfiguration(BaseConfiguration):
    """
    This object inherits the BaseConfiguration object
    """
    DEBUG = True
