from addressbook import Record, AddressBook
from decorators import input_error


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_change_contact(args, book: AddressBook):
    name, phone, *_ = args
    message = "Contact updated."
    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added"

    if phone:
        record.add_phone(phone)

    
    return message


# @input_error
# def change_contact(args, contacts):
#     name, phone = args
    
#     for contact in contacts:
#         if name == contact:
#             contacts[contact] = Record(name).add_phone(phone)

#     return "Contact changed."


@input_error
def show_phone(args, book: AddressBook):
    contact_name = args[0]
    return book.find(contact_name)

    


@input_error
def show_contacts(books: AddressBook):
    result = ""
    for _, record in books.items():
        result += f"\n{record}" if result else f"{record}"

    return f"All contacts:\n{result}"


t1 = Record("test")
t1.add_phone("0000000000")
t1.add_phone("1111111111")

a = AddressBook()
a.add_record(t1)
