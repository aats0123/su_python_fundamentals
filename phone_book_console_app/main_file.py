from find_contact import *
from edit_contact import *

if __name__ == '__main__':
    INPUT_PROMPT = """"Please enter your choise:
    1.Find contact by name
    2.Find contact by town
    3.Find contact by phone number
    4.Print all contacts
    5.Add new contact
    6.Delete contact
    7.Edit contact\n"""
    _input = input(INPUT_PROMPT)

    command_dict = {
        '1': find_contact_by_name,
        '2': find_contact_by_town,
        '3': find_contact_by_phone,
        '4': print_all_contacts,
        '5': add_contact,
        '6': delete_contact,
        '7': edit_contact
    }
    command_dict[_input]()
