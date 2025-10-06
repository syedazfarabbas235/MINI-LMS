from student import Student

class StudentList:
    """
    A manual list class to manage Student objects.
    - Supports fixed size but can expand dynamically.
    - Implements custom add, insert, search, update, and remove operations.
    """

    def __init__(self, capacity=3):
        self._capacity = capacity                 # Maximum number of students allowed initially
        self._students = [None] * self._capacity  # Preallocate space with None
        self._size = 0                            # Current number of students in list

    # ---------- Display ----------
    def display(self):
        """
        Displays the full student list using each student's assigned roll_no.
        """
        print("Student List: \n")
        
        for student in self._students:
            if student is not None:
                print(f"Roll No: {student.roll_no}  {student}")  # Show assigned roll_no and student

        print("=" * 40)


    # ---------- Expand List ----------
    def expand_list(self, extra_slots=2):
        """
        Expands the current capacity of the student list by given extra slots.
        """
        self._students += [None] * extra_slots
        self._capacity += extra_slots

    # ---------- Add Student ----------
    def add_student(self, student):
        """
        Adds a new student to the end of the list.
        """
        if self._size >= self._capacity:
            self.expand_list()

        self._students[self._size] = student
        self._size += 1


    # ---------- Add Student Anywhere ----------
    def add_on(self, student, position):
        """
        Adds a student at a specific position (not necessarily at the end).
        """
        if not (0 <= position <= self._size):
            raise IndexError("Invalid position to add student.")
        if self._size >= self._capacity:
            self.expand_list()

        # Shift students to the right
        for i in range(self._size, position, -1):
            self._students[i] = self._students[i - 1]

        self._students[position] = student
        self._size += 1

    # ---------- Search Student ----------
    def search_student(self, query):
        """
        Searches for a student by name or roll number.
        Returns the index of the student if found, else none
        """
        index = 0  # manual counter
        for student in self._students:
            if student is not None:
                if student.name.lower() == query.lower() or student.roll_no.lower() == query.lower():
                    return index  # ✅ return the found index
            index += 1  # move to next position
        return None  # ❌ not found 
    


    def display_search_result(self, query):
        """
        Displays the search result for a student by name or roll number.
        Shows the index and student details if found.
        """
        index = self.search_student(query)  # Call the search function

        if index is not None:
            student = self._students[index]  # Get the student object
            print(f"🎯 Student found at index {index}")
            print("-" * 40)
            student.display()  # Use Student’s own display() method
            print("=" * 40)
        else:
            print(f"❌ No student found with name or roll number: {query}")
            print("=" * 40)

    # ---------- Update Student ----------
    def update_student(self, query, new_student):
        """
        Updates an existing student record (found by name or roll number)
        with new student details.

        Args:
            query (str): The name or roll number of the student to update.
            new_student (Student): The new student object with updated details.
        """
        for i in range(self._size):  # Loop through active students
            student = self._students[i]
            if student is not None:
                # Match by name or roll number (case-insensitive)
                if student.name.lower() == query.lower() or student.roll_no.lower() == query.lower():
                    
                    self._students[i] = new_student  # Replace the old record
                    return


    def remove_student(self, query):
        """
        Removes a student from the list based on name or roll number.

        Args:
            query (str): The name or roll number of the student to remove.
        """
        for i in range(self._size):  # Loop through active students only
            student = self._students[i]
            if student is not None:
                # Match by name or roll number (case-insensitive)
                if student.name.lower() == query.lower() or student.roll_no.lower() == query.lower():

                    # Shift all subsequent students one position left
                    for j in range(i, self._size - 1):
                        self._students[j] = self._students[j + 1]

                    # Set the last slot to None since it's now empty
                    self._students[self._size - 1] = None

                    # Decrease the active size
                    self._size -= 1
                    return
        
