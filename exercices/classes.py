class student:
    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name

    def greeting (self):
        return f"Hello I am {self.first_name} {self.last_name}"

# let's creat a subclass
class college_student (student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major

class Noncollegestudent (student):
    def __init__(self, first_name, last_name, job):
        super().__init__(first_name, last_name)
        self.job = job

student1 = student('Ben', 'Mulumba', 'Math')
student2 = student('Fally', 'Ipupa', 'Doctor')

print(student1.major)
print(student2.job)
print(student1.greeting())
print(student2.greeting())