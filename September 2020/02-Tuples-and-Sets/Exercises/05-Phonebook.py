phonebook = {}
while True:
    contacts = input().split("-")
    if len(contacts) == 1:
        break
    name = contacts[0]
    number = contacts[1]

    if name not in phonebook:
        phonebook[name] = number
    else:
        phonebook[name] = number

for i in range(int(contacts[0])):
    contact = input()

    if contact in phonebook:
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")