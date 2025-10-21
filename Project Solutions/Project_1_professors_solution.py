class Student:
    def __init__(self, id, first, last):
        self.id = id
        self.first = first
        self.last = last

    def set_GPA(self, GPA):
        self.GPA = float(GPA)
        if self.GPA < 2.0:
            self.probation = True
            print(f"{self.first} {self.last} is in bad academic standing.")
        elif self.GPA >= 2.0:
            self.probation = False
            print(f"{self.first} {self.last} is in good academic standing.")
        return self.probation
        
student_1 = Student(1, "John", "Johnson")
student_2 = Student(2, "Jane", "Doe")
student_3 = Student(3, "Kimberly", "Kim")
student_4 = Student(4, "Will", "Williams")

enrolled_students = [student_1, student_2, student_3, student_4]

student_probation = {}

def display_all(list_of_students):
    for student in list_of_students:
        print(f"{student.first} {student.last}, ID: {student.id}")

def enter_GPA(list_of_students, student_probation):
    student_id = int(input("Enter the ID of the student whom you want to edit."))
    for student in list_of_students:
        if student_id == student.id:
            print(f"You selected to edit the GPA of student {student.first} {student.last}")
            new_GPA = float(input("Enter the new GPA for this student: "))
            probation_status = student.set_GPA(new_GPA)
            student_probation[student.id] = probation_status
            break

def display_probation(student_probation):
    student_id = int(input("Enter the ID of the student of whom you wan to look up their probation status."))
    if student_id in student_probation: 
        if student_probation[student_id] == True:
            print("This student is under academic probation.")
        else:
            print("This student is in good academic standing.")
    else:
        print("This student does not exist or has not been assigned a GPA.")

while(True):
    answer = int(input("\nPlease choose one of the following options: \n" \
    "1. See the list of all enrolled students.\n" \
    "2. Enter a student's GPA. \n" \
    "3. Do a quick lookup to see if a student is under academic probation."))
    #"4. Enroll a new student.\n" 
    if(answer == 1):
        display_all(enrolled_students)
    elif(answer == 2):
        enter_GPA(enrolled_students, student_probation)
    elif(answer == 3):
        display_probation(student_probation)
    else:
        print("Invalid input.")