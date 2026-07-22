class Students:
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        
        
student1 = Students("Abhishek", 101, 21)
student1.add_marks("Math", 85)
student1.add_marks("Science", 90)
student1.add_marks("English", 78)
student1.display_info()
