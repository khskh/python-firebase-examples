"""
Uploads your files to Firebase Storage.

Remember to install firebase-admin and use your own cred.json file.

You can install it by following the command:
    pip install firebase-admin

"""

import firebase_admin
from firebase_admin import credentials, storage
import time

class Uploader:
    def __init__(self, service_account_key_path):
        self.service_account_key_path = service_account_key_path
        self.current_bucket = None
        self.initialize_firebase_app()

    def initialize_firebase_app(self):
        cred = credentials.Certificate(self.service_account_key_path)
        firebase_admin.initialize_app(cred)

    def upload_file(self, local_file_path, remote_file_path, bucket_name):
        blob = storage.bucket(bucket_name).blob(remote_file_path)
        blob.upload_from_filename(local_file_path)

if __name__ == "__main__":
    # Here, specify the location of your 'cred.json' file
    uploader = Uploader(service_account_key_path='cred.json')


    """
    Remember to specify the file name you are uploading, as well as the name it will be saved under on the server.
    You don't need to provide file name extensions for files being uploaded to the server. Example below:
    """
    data = [
        {"local_path": "your_data1.png",                    "remote_path": "your_data1"},
        {"local_path": "your_data2.png",                    "remote_path": "your_data2.png"},
        {"local_path": "your_data3.json",                   "remote_path": "your_data3"},
        {"local_path": "your_data4.json",                   "remote_path": "your_data4.json"},
    ]


    """
    In the 'bucket-name' variable, provide the name of your bucket to which you are uploading files.
    This is an example method for sending files from the 'data' list
    """
    for file_info in data:
        uploader.upload_file(file_info["local_path"], file_info["remote_path"], 'your-bucket-name')
        time.sleep(1)
    print("Storage Updated")