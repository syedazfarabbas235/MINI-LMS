class Person:
    def __init__(self, name, gender, age, email, address):
        if isinstance(name, Person):
            # Copy constructor
            self._name = name._name
            self._gender = name._gender
            self._age = name._age
            self._email = name._email
            self._address = name._address
        else:
        
            self._name = self._validate_name(name)
            self._gender = self._validate_gender(gender)
            self._age = self._validate_age(age)
            self._email = self._validate_email(email)
            self._address = self._validate_address(address)


     # ---------- Properties ----------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_name(value)

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = self._validate_gender(value)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._validate_age(value)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = self._validate_email(value)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = self._validate_address(value)
        


    # ---------- Validation ----------
    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        return name
        
        
    def _validate_gender(self, value):
        if value not in ("Male", "Female", "Other"):
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'.")
        return value

    def _validate_age(self, age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        return age

    def _validate_email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        return email

    def _validate_address(self, address):
        if not isinstance(address, str):
            raise TypeError("Address must be a string.")
        return address

    # ---------- Display ----------
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Gender : {self.gender}")
        print(f"Age    : {self.age}")
        print(f"Email  : {self.email}")
        print(f"Address: {self.address}")

    # ---------- String Representation ----------
    def __str__(self):
        return f" Name:{self.name}, Gender:{self.gender}, Age:{self.age}, Email: {self.email}, Address: {self.address}"
