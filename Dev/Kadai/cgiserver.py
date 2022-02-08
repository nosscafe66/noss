#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "CgiServer Up"
__command__ = "python cgiserver.py"
import http.server
http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)