class Student:
    def __init__(self, name):
        self.name = name  
    def getName(self):
        return self.name
        
class StudentInfo(Student):
    def __init__(self, name, id):
        self.id = id
    def getID(self):
        return self.id
        
class StudentGradeInfo(StudentInfo):
    def __init__(self, name, id, grade):
        Student.name = name
        StudentInfo.id = id
        self.grade = grade
    def getGrade(self):
        return self.grade
    
def main():
    sgi1 = StudentGradeInfo("Julie", "0001111", "A")
    print(sgi1.getName(), sgi1.getID(), sgi1.getGrade())

main()