#!/usr/bin/python3.9
# Test

### Imports ###

import os
from Groups import *
from Content import *
from Print import *
from Management import *

### Variables ###

# Name of the connected user. "None" if none.
username = os.environ.get('REMOTE_USER')

### Body ###

Print(Content(contents, Groups(users, username)))
