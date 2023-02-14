# Returns true if the content's groups overlap with the users group, false otherwise
def ContentIsAllowed(content, user_groups):
    for group in content:
        for user_group in user_groups:
            if group == user_group or group == "everyone":
                return True
    return False

# Returns the weight property of a given content entity
def ReturnWeight(element):
    return element[4]

# Sorts content by decreasing weight
def SortContent(content):
    return sorted(content, key = ReturnWeight, reverse = True)

# Returns contents to be displayed to the user, sorted by decreasing weight
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
