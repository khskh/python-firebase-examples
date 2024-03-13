import firebase_admin
from firebase_admin import db, credentials
from typing import Any


class FirebaseLogUpdate:
    def __init__(self, cert_file, db_reference_url, db_location_ref, MAX_LENGTH):
        if not isinstance(MAX_LENGTH, int) or MAX_LENGTH < 1 or MAX_LENGTH > 9999:
            raise ValueError("MAX_LENGTH must be an integer between 1 and 9999.")

        # var
        self.cert_file = cert_file
        self.db_reference_url = db_reference_url
        self.MAX_LENGTH = MAX_LENGTH
        self.db_location_ref = db_location_ref

        # firebase init
        self.__firebase_init()

    def __firebase_init(self):
        cred = credentials.Certificate(self.cert_file)
        firebase_admin.initialize_app(cred, {'databaseURL': self.db_reference_url})

    def __shift_elements_down(self, data: dict[str, str]) -> dict[str, str]:
        keys = list(data.keys())

        if len(data) > 1:
            for i in range(len(data) - 1, 0, -1):
                data[keys[i]] = data[keys[i - 1]]
            data['el_0001'] = ''
        else:
            if 'el_0001' in data:
                data['el_0002'] = data['el_0001']
                data['el_0001'] = ''
        return data

    def update(self, data_to_add) -> None:
        db_ref = db.reference(self.db_location_ref)
        file_overwrites_data: Any = db_ref.get()

        if not file_overwrites_data:
            file_overwrites_data = {'el_0001': data_to_add}
            db_ref.update(file_overwrites_data)
            return

        if file_overwrites_data['el_0001'] == data_to_add:
            return

        if len(file_overwrites_data) < self.MAX_LENGTH:
            new_list_key = f"el_{len(file_overwrites_data) + 1:04}"
            file_overwrites_data[new_list_key] = ''
            file_overwrites_data = self.__shift_elements_down(file_overwrites_data)

        else:
            file_overwrites_data = self.__shift_elements_down(file_overwrites_data)

        file_overwrites_data['el_0001'] = data_to_add
        db_ref.update(file_overwrites_data)


if __name__ == '__main__':

    # configure before use
    my_db = FirebaseLogUpdate(
        cert_file="path/to/your/cert_file.json",
        db_reference_url="https://your-database-url.firebasedatabase.app/",
        db_location_ref="/path/to/database/location/your_new_db",
        MAX_LENGTH=25
    )

    # example usage
    while True:
        user_input = input()
        my_db.update(user_input)