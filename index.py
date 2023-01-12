#!/usr/bin/python3.9

import os

# Name of the connected user. "None" if none.
username = os.environ.get('REMOTE_USER')

### Functions ### 

# Returns the groups assigned to a name
def Groups(name):
    users = {
        "None": ("everyone"),
    }

    if users[name]:
        return users[name]
    else:
        return users["None"]

# Returns the groups a the user is part of
def Contents(groups):
    contents = [
        ["Website", ("everyone"), "https://frolov.eu", False],
    ]
    for item in contents:
        for group in item[1]:
            a = 1


