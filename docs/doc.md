## How it works

The page the user sees is the output of a Python script.

The script itself is devided into two pieces:

- The "Management" part is used to store information about users and content
- The "Main" part is used to display the page.

Since the scale of my project is very small, I decided to hardcode users and content into Python lists rather than work with text files.

## Configuration guide

!!! info "This documentation expects you to have a working Apache server."

!!! info "Python is required"

!!!note "This is intended for Debian"
    The process might be slightly different with other flavours.

### Script configuration

Copy the contents of the release to `/var/www/html/sharing`.

Make all the `*.py` files executeable by Apache.

!!! info inline end "Default users"
    There are two default users and one default group:

     - Content associated with the "everyone" group is seen by all users regardless of their appartenance
     - "None" is used when a user isn't authenticated. He has access to the "everyone" group
     - "admin" has access to all content.

Everything is managed via 

### Apache configuration

First, create a new directory in `/var/www/html`. Let's name it `sharing`.<br>
Next, paste all the files there and make all the `*.py` files executeable.

Create users that will have access to the page.
First, create the files `/etc/apache2/passwd/passwd` and `/etc/apache2/passwd/groups`.
Next, add users and their passwords using

```
htpasswd /etc/apache2/passwd/passwd username
```

Then open the groups file and add the users to the group `sharing` as follows:

```title="/etc/apache2/passwd/groups" linenums="1"
sharing: user1 user2 user3
```

You need to configure Apache so it would run Python.
The following is to be added into the Apache2 configuration file.
Make sure to customize folder names and anything else you might change.
The following changes are:

 - Allow Apache to run Python scripts
 - Set the index to `index.py`
 - Require authentication to access the directory
     - Users must be part of the "sharing" group

```html title="/etc/apache2/Apache2.conf"
<Directory /var/www/html/sharing/>
    Options Indexes FollowSymLinks ExecCGI
    AddHandler cgi-script /py .cgi
    LoadModule cgi_module /usr/lib/apache2/modules/mod_cgi.so
    AllowOverride None
    Require all granted
    DirectoryIndex index.py
    AuthType Basic
    AuthName "Restricted content'
    AuthUserFile "/etc/apache2/passwd/passwd"
    AuthGroupFile "/etc/apache2/passwd/groups"
    Require group sharing
</Directory>
```

Restart Apache for changes to take effect. 
