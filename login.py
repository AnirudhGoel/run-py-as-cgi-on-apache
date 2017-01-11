#!/usr/bin/python3

import cgi

data = cgi.FieldStorage()
username = data["username"]
password = data["password"]
