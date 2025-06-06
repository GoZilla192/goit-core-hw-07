from addressbook import Record, AddressBook
from decorators import input_error


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
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


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    
    record = book.find(name)

    if record is None:
        return f"Contact \"{name}\" not exists."

    record.edit_phone(old_phone, new_phone)

    return "Contact changed."


@input_error
def show_phone(args, book: AddressBook):
    contact_name = args[0]
    record = book.find(contact_name)
    phones = ""

    if record is None:
        return f"Contact \"{contact_name}\" not exists."

    for phone in record.phones:
        pattern = f"{phone}"
        phones += ', ' + pattern if phones else pattern


    return f"Phones: {phones}"


@input_error
def show_contacts(book: AddressBook):
    result = ""
    for record in book.values():
        result += f"\n{record}" if result else f"{record}"

    return f"All contacts:\n{result}"


@input_error
def add_birthday(args, book: AddressBook):
    contact_name, birthday = args
    record = book.find(contact_name)
    
    if record is None:
        return f"Contact \"{contact_name}\" not exists."
    
    record.add_birthday(birthday)
    
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    contact_name = args[0]
    record = book.find(contact_name)
    if record is None:
        return f"Contact \"{contact_name}\" not exists."
    
    return f"Contact \"{contact_name}\" has a birthday: {record.birthday}"

@input_error
def birthdays(book: AddressBook):
    result = "Contacts who will have a birthday in the next 7 days: "
    upcoming_birthdays = book.get_upcoming_birthdays()

    for record in upcoming_birthdays:
        contact_name = record["name"]
        cong_date = record["congratulation_date"]
        result += f"\n{contact_name}: {cong_date}"

    return result
