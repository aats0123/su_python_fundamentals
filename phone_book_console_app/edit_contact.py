import os
import json
from find_contact import _search


def add_contact():
    input_name = """Please enter contact's first and last name, separated by space:\n"""
    input_phone = """Please enter contact's phone number:\n"""
    input_town = """Please enter contact's town name:\n"""

    name = input(input_name)
    phone_number = input(input_phone)
    town = input(input_town)
    phonebook_entry = {
        'phone': phone_number,
        'name': name,
        'town': town
    }
    phonebook.append(phonebook_entry)
    with open(phonebook_file, 'w+') as ph_book:
        json.dump(phonebook, ph_book)


def delete_contact():
    if len(phonebook) == 0:
        print('Phone book empty!')
    else:
        name = input('Please, enter a name:')
        search_result = _search('name', name, phonebook)
        while len(search_result) > 1:
            name = input(f'More then one result found, please enter correct name:' )
            search_result = _search('name', name, phonebook)
        confirm = input(f"Are you sure that you want to delete {search_result[0]['name']} from the phonebook?[y/n]:").lower()
        if confirm == 'y':
            for entry in phonebook:
                if entry['name'] == search_result[0]['name']:
                    phonebook.remove(entry)
                    with open(phonebook_file, 'w+') as ph_book:
                        json.dump(phonebook, ph_book)
                        print(f"{search_result[0]['name']} deleted")



def edit_contact():
    print('Not implemented')


phonebook_file = os.path.join(os.curdir, 'phonebook.json')
if not os.path.isfile(phonebook_file):
    phonebook = []

else:
    with open(phonebook_file, 'r') as f_phonebook:
        phonebook = json.load(f_phonebook)


