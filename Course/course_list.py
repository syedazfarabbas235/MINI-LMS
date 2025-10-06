from course import Course

class CourseList:
    """
    Manages multiple Course objects.
    - Fixed size, expandable.
    - Supports add, add_on, search, update, and remove.
    """

    def __init__(self, capacity=3):
        self._capacity = capacity
        self._courses = [None] * capacity
        self._size = 0

    # ---------- Display ----------
    def view_course(self):
        print("\n📚 Course List")
        print("=" * 40)
        for i in range(self._size):
            course = self._courses[i]
            print(f"[{i}] {course}")
        print(f"\nTotal Courses: {self._size}/{self._capacity}")
        print("=" * 40)

    # ---------- Expand ----------
    def expand_list(self, extra_slots=2):
        self._courses += [None] * extra_slots
        self._capacity += extra_slots

    # ---------- Add ----------
    def add_course(self, course):
        if self._size >= self._capacity:
            self.expand_list()
        self._courses[self._size] = course
        self._size += 1

    # ---------- Search ----------
    def search_course(self, query):
        index = 0
        for course in self._courses:
            if course is not None:
                if course.course_code.lower() == query.lower() or course.course_name.lower() == query.lower():
                    return index
            index += 1
        return None

    def view_search_course(self, query):
        index = self.search_course(query)
        if index is not None:
            course = self._courses[index]
            print(f"🎯 Course found at index {index}")
            course.display()
            print("=" * 40)
        else:
            print(f"❌ No course found with code or name: {query}")

    # ---------- Update ----------
    def update_course(self, query, new_course):
        for i in range(self._size):
            course = self._courses[i]
            if course is not None:
                if course.course_code.lower() == query.lower() or course.course_name.lower() == query.lower():
                    self._courses[i] = new_course
                    return True
        return False

    # ---------- Remove ----------
    def remove_course(self, query):
        for i in range(self._size):
            course = self._courses[i]
            if course is not None:
                if course.course_code.lower() == query.lower() or course.course_name.lower() == query.lower():
                    for j in range(i, self._size - 1):
                        self._courses[j] = self._courses[j + 1]
                    self._courses[self._size - 1] = None
                    self._size -= 1
                    return True
        return False
