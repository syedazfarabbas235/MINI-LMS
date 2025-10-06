from teacher import Teacher

class TeacherList:
    """
    Manages multiple Teacher objects.
    - Fixed size, expandable.
    - Supports add, search, update, remove, and view operations.
    """

    def __init__(self, capacity=3):
        self._capacity = capacity
        self._teachers = [None] * capacity
        self._size = 0

    # ---------- Display ----------
    def display_teacher(self):
        print("\n👩‍🏫 Teacher List")
        print("=" * 40)
        for i in range(self._size):
            teacher = self._teachers[i]
            print(f"[{i}] {teacher}")
        print(f"\nTotal Teachers: {self._size}/{self._capacity}")
        print("=" * 40)

    # ---------- Expand ----------
    def expand_list(self, extra_slots=2):
        self._teachers += [None] * extra_slots
        self._capacity += extra_slots

    # ---------- Add ----------
    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Only Teacher objects can be added.")

        if self._size >= self._capacity:
            self.expand_list()

        self._teachers[self._size] = teacher
        self._size += 1

    # ---------- Search ----------
    def search_teacher(self, query):
        """
        Searches by employee ID or name.
        Returns index if found, else None.
        """
        index = 0
        for teacher in self._teachers:
            if teacher is not None:
                if teacher.employee_id.lower() == query.lower() or teacher.name.lower() == query.lower():
                    return index
            index += 1
        return None

    def view_search_teacher(self, query):
        """
        Displays teacher details for a given query.
        """
        index = self.search_teacher(query)
        if index is not None:
            teacher = self._teachers[index]
            print(f"🎯 Teacher found at index {index}")
            teacher.display()
            print("=" * 40)
        else:
            print(f"❌ No teacher found with name or employee ID: {query}")

    # ---------- Update ----------
    def update_teacher(self, query, new_teacher):
        """
        Updates a teacher record based on name or employee ID.
        """
        for i in range(self._size):
            teacher = self._teachers[i]
            if teacher is not None:
                if teacher.employee_id.lower() == query.lower() or teacher.name.lower() == query.lower():
                    self._teachers[i] = new_teacher
                    return True
        return False

    # ---------- Remove ----------
    def remove_teacher(self, query):
        """
        Removes a teacher from the list by name or employee ID.
        """
        for i in range(self._size):
            teacher = self._teachers[i]
            if teacher is not None:
                if teacher.employee_id.lower() == query.lower() or teacher.name.lower() == query.lower():
                    for j in range(i, self._size - 1):
                        self._teachers[j] = self._teachers[j + 1]
                    self._teachers[self._size - 1] = None
                    self._size -= 1
                    return True
        return False
