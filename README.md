# Firebase python examples
Some of python scripts for Firebase divided into two groups; local and server-side. All local scripts are intended
to use on your pc, while server-side functions are ready-to-use functions to implement them as Firebase Functions.

Most functions require the installation of the firebase-admin library to work correctly. 
You can install it by following the command:

```
pip install firebase-admin
```

For individual scripts, more information can be found in the requirements.txt
or in a separate README.md file in the script directory.

The detailed description of the usage can be found in the comments within the script

## Local Scripts

[List all UID](local/list_all_UID_with_date) -  Downloads and prints all users UID with creation date.

[Storage Upload](local/storage_uploader) - Uploads your local files to your Firebase Storage.

[Delete inactive users](local/delete_old_UID) -  Function removes all users who have not been active within the last 30 days.

[Realtime Database data logger](local/storage_uploader) - in progress


## Server-Side Scripts

[Delete inactive users](server-side/delete_old_UID) -  Function removes all users who have not been active within the last 30 days.
Function utilizes Google Scheduler - remember to enable this feature in your Google Cloud project (not in Firebase).
