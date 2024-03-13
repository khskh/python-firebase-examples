# Firebase Python Data Logger - RealtimeDatabase

Simple Python class that allows updating data in the Firebase Realtime Database.

- Script add new data at the top of the list in the database and
automatically shift existing data down.

- Script responds only to changes; only a new element with a new,
different name than the previous one will be added to the database.
- You can set maximum number of stored elements in database (maximum number of elements at the moment is 9999).
While updating, last element is automatically deleted.

## Installation
To use it, you need to have the `firebase_admin` library installed.
You can install it using the following command:

```bash
pip install firebase_admin
```

## Usage
Create an instance of the FirebaseLogUpdate class by providing the required parameters:
- **cert_file:** the path to the Firebase service account certificate file.
- **db_reference_url:** the URL of the Firebase Realtime Database.
- **db_location_ref:** the path to the location in the database to be updated.
- **MAX_LENGTH:** the maximum number of items in the database.

*If path doesn't exist, the program automatically creates a new path in Realtime Database*

**Example:**
```python
my_db = FirebaseLogUpdate(
    cert_file="path/to/cert_file.json",
    db_reference_url="https://your-database-url.firebasedatabase.app/",
    db_location_ref="/path/to/database/location/your_new_db",
    MAX_LENGTH=25
)
```

To use the program, you call the update() function on the created object
and give it the data to be stored in the database as a parameter.

**Example**

```python
my_db.update("your_data")
```

## Example usage with data

Providing these data as input `[first, second, third, 4th, 5th, 6th, etc, etc, etc, 7th, 7th]` into these code:
```python
while True:
    user_input = input()
    my_db.update(user_input)
```
We get such a result in the database:

![example-git-firebase](https://github.com/khskh/python-firebase-examples/assets/26013076/3011d59f-6ff0-4a26-aa77-071b7d802180)


## License

Distributed under the MIT License. See LICENSE.txt for more information.
