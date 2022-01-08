import json


def data():

    name = input("Input Your firstname: ")
    surname = input("Input Your lastname: ")
    address = input("Input Your Address: ")
    age = input("Input Your age: ")

    while not age.isdigit():
        user_age = input("Input correct value (age): ")

    return {
        'name': name,
        'surname': surname,
        'address': address,
        'age': age
    }


with open('data_file.json', 'a+', encoding='utf-8') as f:
    lis = []
    for i in range(4):
        lis.append(data())
    f.write(json.dumps(lis, indent=4))
