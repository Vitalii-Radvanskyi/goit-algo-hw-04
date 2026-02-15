def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, new_phone = args
    if not name in contacts:
        return "Contact not found."
    contacts[name] = new_phone
    return "Contact updated."

def show_phon(args, contacts):
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    if not name in contacts:
        return "Contact not found."
    return contacts[name]
def show_all(contacts):
    if not contacts:
        return "No contacts seved."
    line = []
    for name, phone in contacts.items():
        line.append(f"{name}:{phone}")
    return "\n".join(line)
def parse_input(user_input):
    parts = user_input.strip().split()
    commond = parts[0].lower() if parts else ""
    args = parts[1:]
    return commond, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input('Enter command: ')
        command, args = parse_input(user_input)
        if command == "hello":
            print("How can I help you?")   
        elif command == "add":
            print(add_contact(args, contacts))    
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phon(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ("close","exit"):
            print("Good bye!")
            break
        else:
            print("Invalid comand.")
            
if __name__ =="__main__":
    main()