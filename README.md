MITM Proxy
==========

A simple Python WSGI application that forwards all requests to a
target host and returns its responses. Ideally, both the client and
the target host should not be aware that the request is being proxied.

Installation
------------

Run the following commands:

    pip install -r requirements.txt
    export FLASK_DEBUG=1
    flask run

Then, point your web browser to http://localhost:5000/