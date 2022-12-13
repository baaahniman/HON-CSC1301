from Course import *
class Courses:

	# constructor
    def __init__(self):
        self._data = {}

	# add course c to dictionary; do not add if course number already exists
    def add_course(self,c: Course) -> None:
        if c.get_cno() not in self._data:
            self._data[c.get_cno()] = c

	# return True if cno is in dictionary, False otherwise
    def is_course(self,cno):
        if cno in self._data:
            return True
        else:
            return False

	# return a list of all course numbers
    def get_course_numbers(self):
        return self._data.keys()

	# return course object for cno; return None if no course with cno
    def get_course(self,cno):
        if cno in self._data:
            return self._data[cno]
        else:
            return None

	# return string representation of courses object(leave it dont change it!!!)
    def __str__(self):
        result = ''
        for cno in self._data:
            result = result + str(self._data[cno]) + '\n'
        return result
