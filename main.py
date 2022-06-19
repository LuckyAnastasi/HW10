from collections import UserDict


# The parent class for all fields is the general logic for all fields
class Field:

    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


"""
Class that is responsible for the logic of adding / removing / editing optional fields and storing the required field Name
"""


class Record:
    # Initialization
    def __init__(self, name, phone=None, other_phone=None) -> None:
        self.name = name
        self.other_phone = other_phone
        self.phones = []
        if phone:
            self.phones.append(phone)

    # adding fields
    def add_phone(self, phone: Phone):
        for p in self.phones:
            if phone.value == p.value:
                return f'Phone {p} in record'
            else:
                self.phones.append(phone)
                return f'Phone {phone.value} add successful'

    # removing fields
    def del_phone(self, phone: Phone):
        for p in self.phones:
            if phone.value == p.value:
                self.phones.remove(p)
                return f'Phone {phone.value} removed successful'

    # editing fields
    def edit_phone(self, phone: Phone, other_phone: Phone):
        for p in self.phones:
            if phone.value == p.value:
                self.phones.remove(p)
            if other_phone != p.value:
                self.phones.append(other_phone)
                return f'Phone {phone.value} edited on {other_phone.value}'

    # make dict
    def __repr__(self) -> str:
        return f'{self.name.value} : {[p.value for p in self.phones]}'

    # def __repr__(self) -> str:
    #     return f'{[p.value for p in self.phones]}'


# Search logic for records of this class
class AddressBook(UserDict):

    def add_record(self, rec):
        self.data[rec.name.value] = rec


if __name__ == '__main__':
    # fulling class
    name_new = Name("Andrii")
    print(name_new.value)

    phone_first = Phone("+380502720876")
    print(phone_first.value)

    rec = Record(name_new, phone_first)
    print(rec)

    phone_second = Phone("+38095333501")
    print(phone_second.value)

    rec.add_phone(phone_second)
    # rec.del_phone(phone_first)
    # rec.edit_phone(phone_first, phone_second)

    ab = AddressBook()
    ab.add_record(rec)
    print(ab)
