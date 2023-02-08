#!/usr/bin/python3.9

import os
import User
import Content
import Print

### Variables ###

# Name of the connected user. "None" if none.
username = os.environ.get('REMOTE_USER')

### Body ###

user_groups = User.Groups(username)
content = Content.List(user_groups)

print("Content-type: text/html\n\n")
Print.Content(content)
