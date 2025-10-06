class Course:
    """
    Represents a university course with details like code, name, credit hours, and semester.
    Instructor info will be linked later via Teacher class.
    """

    def __init__(self, course_code, course_name, credit_hours, semester_offered):
        self._course_code = self._validate_course_code(course_code)
        self._course_name = self._validate_course_name(course_name)
        self._credit_hours = self._validate_credit_hours(credit_hours)
        self._semester_offered = self._validate_semester_offered(semester_offered)

    # ---------- Properties ----------
    @property
    def course_code(self):
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        self._course_code = self._validate_course_code(value)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = self._validate_course_name(value)

    @property
    def credit_hours(self):
        return self._credit_hours

    @credit_hours.setter
    def credit_hours(self, value):
        self._credit_hours = self._validate_credit_hours(value)

    @property
    def semester_offered(self):
        return self._semester_offered

    @semester_offered.setter
    def semester_offered(self, value):
        self._semester_offered = self._validate_semester_offered(value)

    # ---------- Validation ----------
    def _validate_course_code(self, code):
        if not isinstance(code,(str,int)):
            raise ValueError("Course code must be a non-empty string.")
        return code

    def _validate_course_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Course name must be a non-empty string.")
        return name

    def _validate_credit_hours(self, hours):
        if not isinstance(hours, int) or hours <= 0 or hours > 5:
            raise ValueError("Credit hours must be between 1 and 5.")
        return hours

    def _validate_semester_offered(self, semester):
        if not isinstance(semester, str):
            raise ValueError("Semester offered must be a non-empty string.")
        return semester

    # ---------- Display ----------
    def display(self):
        print("📘 Course Details")
        print("=" * 30)
        print(f"Course Code      : {self.course_code}")
        print(f"Course Name      : {self.course_name}")
        print(f"Credit Hours     : {self.credit_hours}")
        print(f"Semester Offered : {self.semester_offered}")
        print("=" * 30)

    # ---------- String Representation ----------
    def __str__(self):
        return f"{self.course_code} - {self.course_name} ({self.credit_hours} Cr.Hrs), Semester: {self.semester_offered}"
