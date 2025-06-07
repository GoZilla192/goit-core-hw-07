from datetime import datetime, date, timedelta
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

    

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            self.value = value

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    

    def __str__(self):
        return self.value
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)


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
                return 
            
        raise ValueError(f"Phone number {old_phone} does not exist")
    

    def find_phone(self, search_phone: str) -> Union[Phone, None]:
        for phone in self.phones:
            if phone.value == search_phone:
                return phone


    def __str__(self):
        return f"Contact name: {self.name.value}; phones: {', '.join(p.value for p in self.phones)}; birthday: {self.birthday}"


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


    def _find_next_weekday(self, start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)


    def _adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self._find_next_weekday(birthday, 0)
        
        return birthday

    def get_upcoming_birthdays(self) -> list[dict]:
        upcoming_birthdays = []
        today = date.today()

        for name, record in self.data.items():
            if record.birthday is None:
                continue

            birthday_this_year = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()          
            birthday_this_year = birthday_this_year.replace(year=today.year)
 
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)
           
            if 0 <= (birthday_this_year - today).days <= 7:
                birthday_this_year = self._adjust_for_weekend(birthday_this_year)
                
                congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
                upcoming_birthdays.append({"name": name, "congratulation_date": congratulation_date_str})


        return upcoming_birthdays
    
