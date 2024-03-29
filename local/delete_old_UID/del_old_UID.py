"""
The function removes all users who have not been active within the last 30 days.

Remember to install firebase-admin and use your own cred.json file.

You can install it by following the command:
    pip install firebase-admin

"""

import firebase_admin
from firebase_admin import credentials, auth
from datetime import datetime, timedelta

cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred)

def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

def remove_inactive_users():

    current_time = datetime.now()

    for user in auth.list_users().iterate_all():

        last_sign_in_time = user.user_metadata.last_sign_in_timestamp

        if last_sign_in_time is not None:
            last_sign_in_time = datetime.fromtimestamp(last_sign_in_time / 1000.0)
            time_difference = current_time - last_sign_in_time
            if time_difference.days > 30:
                auth.delete_user(user.uid)
                print('User with UID: ' + user.uid + ' deleted.')
        else:

            auth.delete_user(user.uid)
            print('User with UID: ' + user.uid + ' deleted.')
    print('All inactive users for more than 30 days have been removed.')


if __name__ == '__main__':
    remove_inactive_users()
