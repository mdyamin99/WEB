class Student():
    def __init__(self,name,c_class,id):
        self.name = name
        self.c_class = c_class
        self.id = id
    def __repr__(self)->str:
        return f'Student with name: {self.name} class: {self.c_class} id: {self.id}'


class Teacher():
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self)->str:
        return f'Teacher name: {self.name} subject: {self.subject}'   
    

class School():
    def __init__(self,name):
        self.name = name
        self.teacher = []
        self.student = []

    def add_teacher(self,name,subject):
        id = len(self.teacher) + 101
        teacher = Teacher(name,subject,id)
        self.teacher.append(teacher)

    def enroll(self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.student) + 1
            student = Student(name,'C',id)
            self.student.append(student)
            return f'{name} is enrolled id: {id}, extra money {fee - 6500}'
        
    def __repr__(self)->str:
        print('Welcome to', self.name)
        print('------Our Teacher------')
        for teacher in self.teacher:
            print(teacher)
        print('-------Our Student------')
        for student in self.student:
            print(student)
        return 'all done for now'



# alia = Student('Alia torkari',9,100)
# ranbeer = Teacher('Douran beer','Algorithm',101)
# print(ranbeer)
# print(alia)


phitron = School('Phitron')
phitron.enroll('alia',5200)
phitron.enroll('rani',8000)
phitron.enroll('aweisariya',9000)
phitron.enroll('vaijan',90000)
phitron.enroll('ami',6500)

phitron.add_teacher('Tom Cruise','Algo')
phitron.add_teacher('Decap','DS')
phitron.add_teacher('AJ','Database')
print(phitron)
