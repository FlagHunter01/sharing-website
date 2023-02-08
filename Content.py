# Tells if content is allowed based on user's groups
def ContentIsAllowed(content, user_groups):
    for group in content:
        for user_group in user_groups:
            if group == user_group or group == "everyone":
                return True
    return False

def ReturnWeight(element):
    return element[4]

def SortContent(content):
    return sorted(content, key = ReturnWeight, reverse = True)

# Returns the groups a the user is part of
def List(user_groups):
    contents = [
        ["Website", "https://frolov.eu", ["everyone"], "link.png", 1],
        ["This is first", "first", ["everyone"], "first.png", 2],
    ]
    allowed_content = list()
    for content in contents:
        if ContentIsAllowed(content[2], user_groups):
            allowed_content.append(content)
    return SortContent(allowed_content)
