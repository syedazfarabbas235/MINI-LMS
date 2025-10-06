from student import Student
from Student_list import StudentList

def main():
    try:
        DCS= StudentList()
       
        # Create Student objects
        s1 = Student("Ali","Male", 20, "ali@gmail.com", "Lahore",
                     "1", "BSCS", 2025, 1, "Paid")
        s2 = Student("Ayesha", "Female", 21, "ayesha@gmail.com", "Karachi",
                     "2", "BSCS", 2025, 1, "Pending")
        s3 = Student("Hassan","Male", 22, "hassan@gmail.com", "Islamabad",
                     "3", "BSCS", 2025, 2, "Unpaid")

        # Add initial students
        DCS.add_student(s1)
        DCS.add_student(s2)
        DCS.add_student(s3)

        DCS.display()

        # Add a new student (triggers automatic expansion if full)
        s4 = Student("Sara","Female", 23, "sara@gmail.com", "Multan",
                     "4", "BSCS", 2025, 3, "Paid")
        DCS.add_student(s4)

        DCS.display()

        # Add a student at a specific position (middle)
        print("Bilal joined and was placed at index 2 \n")
        s5 = Student("Bilal","Male", 21, "bilal@gmail.com", "Faisalabad",
                     "5", "BSCS", 2025, 1, "Paid")
        DCS.add_on(s5, 2)

        DCS.display()

        # Search for a student by name or roll number
        DCS.display_search_result("Sara")


        # Update student record
        print ("Record updated for roll no 2 (ayesha is replaced by ahmed) \n")
        new_student = Student("Ahmed","Male", 21, "ahmed123@gmail.com", "Karachi",
                             "2", "BSCS", 2025, 2, "Paid")
        DCS.update_student("Ayesha", new_student)

        DCS.display()

        # Remove a student by name or roll number
        print("Hassan (roll no 3) left the department \n")
        DCS.remove_student("Hassan")

        DCS.display()

       

    except Exception as e:
        # Catch any exception that occurs in main 
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
