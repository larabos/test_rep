from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(title)
        if title in self.modules:
            self.grades[title] = title.get_grade()

    def get_list_modules(self):
        for module1 in self.modules:
            print('Modules of Student {0}:\n {1}'.format(self.name, module1))

    def get_grades(self):
        for module in self.grades:
            print('Grades of Student {0}: \n {1}: {2}'.format(self.name, module, self.grades[module]))


### test cases ###

me = Student("Lara Bos")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
