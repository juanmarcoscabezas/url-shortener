# Introduction

The goal of this project is to make a URL shortener API. 

### Main features

* We must be able to post an URL into a route/endpoint and get back a new URL with the shortest possible length.

* We must be redirected to the full URL when we enter/send the short URL in a form/endpoint (ex: http://localhost:3000/a => https://google.com)

* There should be an endpoint that returns top 100 most frequently accessed URLs

* There must be a background job that crawls the URL being shortened, pulls the HTML title tag from the website and stores it.

* Display the title with the URL on the top 100 endpoint.

* There must be a README that explains how to setup the application and the algorithm used for generating the URL short code.

* Write a bot to populate your DB, and include it in the source code

* Write Unit or Integration Tests

# Usage

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install packages

    $ pip install -r requirements.txt

And then run the `django-admin.py` command to run the migrations:

    $ python3 manage.py migrate

And then run the `django-admin.py` command to run the project:

    $ python3 manage.py runserver

# HTTP Methods

```http
GET http://127.0.0.1:8000/api/shortener/
Expect [
	{
		"source_url": "https://www.django-rest-framework.org",
		"shortened_url": "http://127.0.0.1:8000/SyamnjHdeaA=",
		"views": 5
	}
]


POST http://127.0.0.1:8000/api/shortener/
Content-Type: application/json
{
	"source_url": "https://www.django-rest-framework.org"
}

Expect {
	"source_url": "https://www.django-rest-framework.org",
	"shortened_url": "http://127.0.0.1:8000/oaSBL4I8NSM=",
	"views": 0
}

GET http://127.0.0.1:8000/oaSBL4I8NSM=
Expect Redirect to https://www.django-rest-framework.org
```


# Algorithm

The algorithm uses a combination of a hash function and base convertion.

```python
import hashlib
import base64

def shorten_url(url):
    # Convert URL to bytes and hash using SHA256
    url_bytes = url.encode('utf-8')
    hash_bytes = hashlib.sha256(url_bytes).digest()

    # Take the first 8 bytes of the hash and base64 encode
    short_bytes = hash_bytes[:8]
    short_url = base64.b64encode(short_bytes).decode('utf-8')

    return short_url
```

# Tests

Run the `django-admin.py` command to run the tests:

    $ python3 manage.py test
