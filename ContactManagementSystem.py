def addContact(contacts, name, phone, email):
    if name in contacts:
        print(f"Contact {name} already exists")
    else:
        contacts[name] = {'Phone': phone, 'email': email}
        print(f"Contact {name} added successfully")


def displayContacts(contacts):
    print("Contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['Phone']},Email: {[info['email']]}")


contacts = {}
addContact(contacts, 'Mounish', '44576765', 'mnsh@gmail.com')
addContact(contacts, 'Mounish1', '144576765', '1mnsh@gmail.com')
print(contacts)
displayContacts(contacts)
