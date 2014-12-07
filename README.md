URL Shortener
================

# Overview

A Flask RESTful web application for creating and tracking shortened URL's.

##### version: Url Shortener BETA 0.1

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

# Usage

|  HTTP Method  |  URI |  Action |
| :-----------: | :--- | :------ |
| GET | http://[hostname]/api/v1.0/tni | Retrieve a list of shortened URLs |
| GET | http://[hostname]/api/v1.0/tni/[tni_url] | Retrieve single shortened URL |

Publically exposed data fields:

##### Fields

- **id:** ID of the shortened URL
- **tni_url:** Our key for the target URL
- **actual_url:** Target URL to redirect to
- **created:** Date shortened URL was created

# Installation

```bash
apt-get update && apt-get install python-dev build-essential python-setuptools python-virtualenv
```

```bash
git clone -b part-1 git@github.com:configuresystems/url-shortener.git application
cd application
virtualenv flast
source venv/bin/activate
# due to weird pip limitations, we have to install ez_setup separately
python run.py runserver -h [HOSTNAME] -p [PORT]
```

Get all requests

```bash
curl -i http://[hostname]/api/v1.0/tni
```

Get single request by tni_url

```bash
curl -i http://[hostname]/api/v1.0/tni/[tni_url]
```

Test Redirection

http://[hostname]/tni/[tni_url]
