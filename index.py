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
def Contents(user_groups):
    contents = [
        ["Website", "https://frolov.eu", ("everyone"), False],
    ]
    allowed_content = list()
    for content in contents:
        for group in content[1]:
            for user_group in user_groups:
                if group == user_group:
                    allowed_content.append(content)
                    break




