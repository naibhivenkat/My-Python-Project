class Student:

        school = "Naibhi"
        def __init__(self, m1, m2, m3):
                self.m1 = m1
                self.m2 = m2
                self.m3 = m3

        def avg(self):
                return (self.m1 + self.m2 + self.m3)/3

        @classmethod
        def info (cls):
                return cls.school

s1 = Student(34,67,32)
s2 = Student(75,35,12)

print(s1.avg(), Student.info())
print(s2.avg(), Student.info())