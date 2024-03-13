import firebase_admin
from datetime import datetime
from firebase_functions import scheduler_fn
from firebase_admin import credentials, auth


cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred)

def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

"""
Function utilizes Google Scheduler - remember to enable this feature in your Google Cloud project (not Firebase).
The CRON expression "0 0 * * *" triggers the function daily at 00:00.
"""

@scheduler_fn.on_schedule(schedule="0 * * * *")
def remove_inactive_users():

    current_time = datetime.now()

    for user in auth.list_users().iterate_all():

        last_sign_in_time = user.user_metadata.last_sign_in_timestamp

        if last_sign_in_time is not None:
            last_sign_in_time = datetime.fromtimestamp(last_sign_in_time / 1000.0)
            time_difference = current_time - last_sign_in_time
            if time_difference.days > 30:
                auth.delete_user(user.uid)
        else:
            auth.delete_user(user.uid)