### List users here ###
# Format: "Username": {"group1", group2},
users = {
    "None": {"everyone"}, # Mandatory
    "admin": {"admin"}, # Mandatory
}


### List contents here ###
# Format: ["Title", "URL", {"group1", "group2"}, "img/image.png", weight],
# The weight must be expressed by an int.
# Contents will be sorted by weight: the heavier will be displayed first
contents = [
    ["Example", "https://example.com/", {"everyone"}, "img/link.png", 1],
]
