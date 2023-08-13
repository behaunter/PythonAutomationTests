import random
import string

class DataObject:

    @staticmethod
    def generate_random_string(length):
        characters = string.ascii_letters 
        return ''.join(random.choice(characters) for i in range(length))

    def generate_user_data():
        firstName_random = DataObject.generate_random_string(10)
        id_random = random.randint(0, 100)
        lastName_random = DataObject.generate_random_string(10)
        email_random = DataObject.generate_random_string(10)
        password_random = DataObject.generate_random_string(10)
        phone_random = DataObject.generate_random_string(10)
        userStatus_random = random.randint(0, 3)

        data = [
        {
            "id": id_random,
            "username": "ghbsdf@S",
            "firstName": firstName_random,
            "lastName": lastName_random,
            "email": email_random,
            "password": password_random,
            "phone": phone_random,
            "userStatus": userStatus_random
        }
    ]
        return data

    def get_username_random():
        return DataObject.generate_random_string(10)

