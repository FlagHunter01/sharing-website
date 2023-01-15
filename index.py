#!/usr/bin/python3.9

import os
import User
import Content

### Variables ###

# Name of the connected user. "None" if none.
username = os.environ.get('REMOTE_USER')

### Body ###

user_groups = User.Groups(username)
content = Content.List(user_groups)

print("Content-type: text/html\n\n")
#with open(file) as file:
#    print(file.read())
for item in content:
    print(item[0] + '''<br>''')

