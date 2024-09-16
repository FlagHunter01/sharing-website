# Returns True if the contents groups and the users groups overlap
def ContentIsAllowed(content_groups, user_groups):
    # Always return True if the user is admin
    if "admin" in user_groups:
        return True
    
    # Always return True if the content is for everyone
    if "everyone" in content_groups:
        return True
    
    # Check if the contets groups and the users groups overlap
    if content_groups.intersection(user_groups):
        return True
    else:
        return False


# Returns the weight property of a given content element
def ReturnWeight(element):
    return element[4]


# Sorts content by decreasing weight
def SortContent(content):
    return sorted(content, key = ReturnWeight, reverse = True)


# Returns contents to be displayed to the user, sorted by decreasing weight
def Content(contents, user_groups):
    allowed_content = list()
    for content in contents:
        if ContentIsAllowed(content[2], user_groups):
            allowed_content.append(content)
    return SortContent(allowed_content)
