from person import Person
from course_list import CourseList 


class Teacher(Person):
    """
    Represents a Teacher (inherits from Person).
    Includes details like employee ID, department, designation, salary, and
    a list of assigned courses (CourseList).
    """

    def __init__(self, name, gender, age, email, address,
                 employee_id, department, designation, salary, course_assigned=None):
        # Initialize Person attributes
        super().__init__(name, gender, age, email, address)

        # Teacher-specific attributes
        self._employee_id = self._validate_employee_id(employee_id)
        self._department = self._validate_department(department)
        self._designation = self._validate_designation(designation)
        self._salary = self._validate_salary(salary)
        self._course_assigned = self._validate_course_assigned(course_assigned)

    # ---------- Properties ----------
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = self._validate_employee_id(value)

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = self._validate_department(value)

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, value):
        self._designation = self._validate_designation(value)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = self._validate_salary(value)

    @property
    def course_assigned(self):
        return self._course_assigned

    @course_assigned.setter
    def course_assigned(self, value):
        self._course_assigned = self._validate_course_assigned(value)

    # ---------- Validation ----------
    def _validate_employee_id(self, emp_id):
        if not isinstance(emp_id, str) or not emp_id.strip():
            raise ValueError("Employee ID must be a non-empty string.")
        return emp_id.strip().upper()

    def _validate_department(self, dept):
        if not isinstance(dept, str) or not dept.strip():
            raise ValueError("Department must be a valid string.")
        return dept.strip().title()

    def _validate_designation(self, desig):
        if not isinstance(desig, str) or not desig.strip():
            raise ValueError("Designation must be a valid string.")
        return desig.strip().title()

    def _validate_salary(self, salary):
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError("Salary must be a positive number.")
        return salary

    def _validate_course_assigned(self, course_list):
        """
        Validates that assigned courses are of type CourseList or None.
        """
        if course_list is None:
            return None
        if not isinstance(course_list, CourseList):
            raise TypeError("Course assigned must be of type 'CourseList' or None.")
        return course_list

    # ---------- Display ----------
    def display(self):
        super().display()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Department      : {self.department}")
        print(f"Designation     : {self.designation}")
        print(f"Salary          : {self.salary}")

        if self.course_assigned and self.course_assigned._size > 0:
            print("\n📘 Assigned Courses:")
            self.course_assigned.view_course()
        else:
            print("Assigned Courses: None")

        print("=" * 40)

    # ---------- String Representation ----------
    def __str__(self):
        base_info = super().__str__()
        if self.course_assigned and self.course_assigned._size > 0:
            course_names = [course.course_name for course in self.course_assigned._courses if course]
            course_list_str = ", ".join(course_names)
        else:
            course_list_str = "None"
        return (f"{base_info}, Emp ID: {self.employee_id}, Dept: {self.department}, "
                f"Designation: {self.designation}, Salary: {self.salary}, "
                f"Courses: {course_list_str}")
