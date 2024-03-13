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

    uploader = Uploader(service_account_key_path='cred.json')

    # list of files to upload
    data = [
        {"local_path": "your_data1.png",                    "remote_path": "your_data1"},
        {"local_path": "your_data2.png",                    "remote_path": "your_data2"},
        {"local_path": "your_data3.json",                   "remote_path": "your_data3"},
        {"local_path": "your_data4.json",                   "remote_path": "your_data4.png"},
    ]

    for file_info in data:
        uploader.upload_file(file_info["local_path"], file_info["remote_path"], 'your-bucket-name')
        time.sleep(1)
    print("Storage Updated")