URL Shortener
================

##### Version: Url Shortener BETA 0.1

# Overview

A Flask RESTful web application for creating and tracking shortened URL's.

# Requirements

Aptitude Packages:

- python-dev
- build-essentials
- python-setuptools
- python-virtualenv

Required PIP packages, also in the requirements.txt

- Flask==0.10.1
- Flask-RESTful==0.3.0
- Flask-Actions==0.6.6
- requests==2.5.0

# Installation

```bash
apt-get update && apt-get install python-dev build-essential python-setuptools python-virtualenv
```

```bash
git clone -b part-1 https://github.com/configuresystems/url-shortener.git application
cd application
virtualenv flask
source flask/bin/activate
python run.py runserver -h [HOSTNAME] -p [PORT]
```

# Usage

|  HTTP Method | Response|  URI |  Action |
| :-----------:|:--:| :--- | :------ |
| GET | JSON | http://[hostname]/api/v1.0/tni | Retrieve a list of shortened URLs |
| GET | JSON | http://[hostname]/api/v1.0/tni/[tni_url] | Retrieve single shortened URL |
| GET | HTML | http://[hostname]/[tni_url] | URL Redirect|

Publically exposed data fields:

##### Fields

- **id:** ID of the shortened URL
- **tni_url:** Our key for the target URL
- **actual_url:** Target URL to redirect to
- **created:** Date shortened URL was created
