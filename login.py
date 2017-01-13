#!/usr/bin/python3

import cgi

data = cgi.FieldStorage()
username = data["username"]
password = data["password"]

print("Content-Type: text/html\n")
print(username)
print(password)