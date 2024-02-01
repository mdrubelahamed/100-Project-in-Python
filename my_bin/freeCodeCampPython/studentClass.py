class Student:
    def __init__(self,name,course,gpa,isPass):
        self.name = name
        self.course = course
        self.gpa = gpa
        self.isPass = isPass

    def Character(self):
        if self.gpa >= 7:
            return True
        else:
            return False