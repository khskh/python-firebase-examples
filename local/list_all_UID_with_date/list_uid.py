"""
Lists all user ID's with creation date.

Remember to install firebase-admin and use your own cred.json file.

You can install it by following the command:
    pip install firebase-admin

"""

import firebase_admin
from firebase_admin import credentials, auth
from datetime import datetime

# Init firebase
cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred)

# Func to format timestamp date
def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')


# print all UID with formatted creation date
for user in auth.list_users().iterate_all():
    print('User UID: ' + user.uid + ', Created At: ' + format_timestamp(user.user_metadata.creation_timestamp))