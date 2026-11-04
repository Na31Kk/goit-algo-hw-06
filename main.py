from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):        
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        user_phone = Phone(phone)
        self.phones.append(user_phone)

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None     

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        new_user_phone = Phone(new_phone)
        old_user_phone = self.find_phone(old_phone)
        if not old_user_phone:
            raise ValueError
        else: 
            ph_index = self.phones.index(old_user_phone)
            self.phones[ph_index] = new_user_phone
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name)

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())