# Prints the HTML with the authorized content
def Print(content):
    print("Content-type: text/html\n\n")
    print('''
    <!DOCTYPE html>
<html>

<head>
    <title>
        Sharing page
    </title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <div class="header">
        Sharing Page
    </div>
    <div class="content">
    ''')
    for item in content:
        print('''
        <a href="''' + item[1] + '''" target="_blanc">
        <div class="card">
            <div class="card_image" style='background-image: url("''' + item[3] + '''")'></div>
            <div class="card_footer">
                <a class="card_link" href="''' + item[1] + '''">''' + item[0] + '''</a>
            </div>
        </div>
        </a>
        ''')
    print('''
        </div>
        <div class="footer"></div>
    </body>

    </html>
    ''')
    return
