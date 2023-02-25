# Prints the HTML with the authorized contentx
def Content(content):
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
        <div class="card">
            <div class="card_image" style='background-image: url("''' + item[3] + '''")'></div>
            <div class="card_footer">
                <a class="card_link" href="''' + item[1] + '''">''' + item[0] + '''</a>
            </div>
        </div>
        ''')
    print('''
        </div>
        <div class="footer"></div>
    </body>

    </html>
    ''')
    return
