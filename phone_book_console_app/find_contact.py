import os
import json
import re


def find_contact_by_name():
    name = input('Please, enter a name:')
    search_result = _search('name', name, phonebook)
    _print(search_result)


def find_contact_by_phone():
    phone = input('Please, enter a phone number:')
    search_result = _search('phone', phone, phonebook)
    _print(search_result)


def find_contact_by_town():
    town = input('Please, enter a town name:')
    search_result = _search('town', town, phonebook)
    _print(search_result)


def print_all_contacts():
    if len(phonebook) == 0:
        print('Phone book empty!')
    else:
        _print(phonebook)


def _search(item, string, ph_book):
    search_result = []
    regex = re.compile(string, re.IGNORECASE)
    for line in ph_book:
        if regex.search(line[item]):
            search_result.append(line)
    return search_result


def _print(result):
    print(f'{len(result)} result(s) found')
    for line in result:
        print(f'Name: {line["name"]}\n\t-Phone: {line["phone"]}\n\t-Town: {line["town"]}')


phonebook_file = os.path.join(os.curdir, 'phonebook.json')

if not os.path.isfile(phonebook_file):
    phonebook = []
else:
    with open(phonebook_file, 'r') as f_phonebook:
        phonebook = json.load(f_phonebook)
