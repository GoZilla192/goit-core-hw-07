from collections import UserDict
from typing import Union


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return self.value
    

    def __repr__(self):
        return self.__str__()


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone_for_remove: str):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_for_remove:
                del self.phones[i]
    

    def edit_phone(self, old_phone: str, new_phone: str):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)

        raise ValueError(f"Phone number {old_phone} does not exist")
    

    def find_phone(self, search_phone: str) -> Union[Phone, None]:
        for phone in self.phones:
            if phone.value == search_phone:
                return phone


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


    def __repr__(self):
        return self.__str__()


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record 


    def find(self, search_name: str) -> Union[Record, None]:
        return self.data.get(search_name)
            

    def delete(self, delete_name: str) -> None:
        self.data.pop(delete_name)
            

    def __str__(self):
        return f"AddressBook {self.data}"
    
