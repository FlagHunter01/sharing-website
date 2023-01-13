# Tells if content is allowed based on user's groups
def ContentIsAllowed(content, user_groups):
    for group in content:
        for user_group in user_groups:
            if group == user_group or group == "everyone":
                return True
    return False

# Returns the groups a the user is part of
def List(user_groups):
    contents = [
        ["Website", "https://frolov.eu", ("everyone"), False],
    ]
    allowed_content = list()
    for content in contents:
        if ContentIsAllowed(content[2], user_groups):
            allowed_content.append(content)
    return allowed_content
