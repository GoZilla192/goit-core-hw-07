from colorama import Fore
from addressbook import AddressBook, Record
from events import *


def main():
    book = AddressBook()
    print("Hello, I your assistent, enter command")

    while True:
        user_input = input(f"{Fore.BLUE}[Assistent]{Fore.RESET} > ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Goodbye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))
        
        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_contacts(book))
        
        elif command == "add-birthday":
            print(add_birthday(args, book))
        
        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
