#!flask/bin/python

# import our application
from app import app
# import a flask manager for multi-threaded
from flask.ext.actions import Manager

if __name__ == '__main__':
    # instantiate Manager as a wrapper for our app
    manager = Manager(app)
    manager.run()
