#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler
 
Server = HTTPServer
handler = CGIHTTPRequestHandler
port = 8080
server_address = ("", port)
# Find CGI scripts in the current working directory.
handler.cgi_directories = [""]
 
httpd = Server(server_address, handler)
print("Server listening on http://{}:{}".format(
    httpd.server_name,
    httpd.server_port
))
httpd.serve_forever()