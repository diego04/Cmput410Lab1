

class Student():
    
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.CourseMarks = {}
        
    def addCourseMark(self, course, mark):
        self.CourseMarks[course]=mark
        self.course = course
    
    def average(self):
        self.averaged = 0
        for key,value in self.CourseMarks.items():
            print key
            self.averaged = self.averaged + value
        return self.averaged/(len(self.CourseMarks))
    
        
        

studentinstance = Student("studentone", "studentlastname")
studentinstance.addCourseMark("compsci", 89)
studentinstance.addCourseMark("english", 99)


print studentinstance.name

print studentinstance.average()



