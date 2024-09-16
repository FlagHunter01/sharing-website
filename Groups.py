# If the username is found, this function returns its associated groups.
# Otherwise, it returns the groups associated to the mandatory "None" user.
def Groups(users, username):    
    if username in users:
        return users[username]
    else:
        return users["None"]
