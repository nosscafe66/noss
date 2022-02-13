#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "WSGI SERVER"

from wsgiref.simple_server import make_server

import os.path

def on_html(environ, start_response):
    path = environ["PATH_INFO"]
    headers = [('Content-type', 'text/html; charset=utf-8')]
    if path in ("", "/"):
        path = "index.html"
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path.lstrip("/"))) as rf:
            status = '200 OK'
            start_response(status, headers)
            return [rf.read()]
    except Exception as e:
        print(e)
        status = '404 Not Found'
        start_response(status, headers)
        return [bytes(path)]