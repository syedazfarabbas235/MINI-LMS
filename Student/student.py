from person import Person

class Student(Person):
    """
    A Student class inheriting from Person.
    Adds admission-related details such as roll number, program, etc.
    """

    def __init__(self, name, gender, age, email, address,
                 roll_no, program, admission_year, semester, fee_status):
        # Initialize parent (Person)
        super().__init__(name, gender, age, email, address)

        # Student-specific attributes with validation
        self._roll_no = self._validate_roll_no(roll_no)
        self._program = self._validate_program(program)
        self._admission_year = self._validate_admission_year(admission_year)
        self._semester = self._validate_semester(semester)
        self._fee_status = self._validate_fee_status(fee_status)

    # ---------- Properties ----------
    @property
    def roll_no(self):
        return self._roll_no

    @roll_no.setter
    def roll_no(self, value):
        self._roll_no = self._validate_roll_no(value)

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, value):
        self._program = self._validate_program(value)

    @property
    def admission_year(self):
        return self._admission_year

    @admission_year.setter
    def admission_year(self, value):
        self._admission_year = self._validate_admission_year(value)

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = self._validate_semester(value)

    @property
    def fee_status(self):
        return self._fee_status

    @fee_status.setter
    def fee_status(self, value):
        self._fee_status = self._validate_fee_status(value)

    # ---------- Validation Functions ----------
    def _validate_roll_no(self, roll_no):
        """
        Validate student roll number.
        Example format: "BSCS-2025-001"
        """
        if not isinstance(roll_no, str):
            raise ValueError("Roll number must be a non-empty string.")
        return roll_no

    def _validate_program(self, program):
        """
        Validate program name.
        """
        if not isinstance(program, str):
            raise ValueError("Program must be a valid non-empty string.")
        return program

    def _validate_admission_year(self, year):
        """
        Validate admission year (1900–2100).
        """
        if not isinstance(year, int) or year < 2021 or year > 2025:
            raise ValueError("Admission year must be between 1900 and 2100.")
        return year

    def _validate_semester(self, semester):
        """
        Validate semester (must be positive integer).
        """
        if not isinstance(semester, int) or semester <= 0:
            raise ValueError("Semester must be a positive integer.")
        return semester

    def _validate_fee_status(self, status):
        """
        Validate fee status (Paid/Unpaid/Pending).
        """
        valid_status = ["Paid", "Unpaid", "Pending"]
        if status not in valid_status:
            raise ValueError(f"Fee status must be one of {valid_status}.")
        return status

    # ---------- Display ----------
    def display(self):
        super().display()  # Call Person’s display
        #print(f"Roll No        : {self.roll_no}")
        print(f"Program        : {self.program}")
        print(f"Admission Year : {self.admission_year}")
        print(f"Semester       : {self.semester}")
        print(f"Fee Status     : {self.fee_status}")
        print("=" * 40)

    # ---------- String Representation ----------
    def __str__(self):
        base_info = super().__str__()
        return (f"{base_info}, Program: {self.program},Admission Year: {self.admission_year}, Semester: {self.semester}, Fee Status: {self.fee_status}")
