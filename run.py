#!flask/bin/python

# import our application
from app import app

# The Flask-Actions extension provides support for writing external actions in
# Flask. This includes running a development server, a customized python
# shell, a fastcgi server like django
# https://pythonhosted.org/Flask-Actions/
from flask.ext.actions import Manager

if __name__ == '__main__':
    # Start up our application when run.py is executed
    manager = Manager(app)
    manager.run()
