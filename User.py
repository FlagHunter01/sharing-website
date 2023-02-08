# Returns the groups assigned to a name
def Groups(name):
    users = {
        "None": ["everyone"],
    }
    key = f'{name}' if name else "None"
    if key in users:
        return users[key]
    else:
        return users["None"]
