from Student import *

class Students:

	# constructor
	def __init__(self):
		self._data = {}

# s is the whole thing, s.get_name() is just the name

	# add student s to dictionary; if student s already present do nothing
	def add_student(self,s):
		if s.get_name() not in self._data:
			self._data[s.get_name()] = s

	# return True of sname is present in dictionary; False otherwise
	def is_student(self,sname):
		if sname in self._data:
			return True
		else:
			return False

	# return a list of all student names
	def get_student_names(self):
		result = []
		for sname in self._data:
			result.append(sname)
		return result

	# return Student object for sname; return None if sname not in dictionary
	def get_student(self,sname):
		if sname in self._data:
			return self._data[sname]
		else:
			return None

	# getter
	def get_students(self):
		return self._data

	# return a list of pairs (sname,gpa) of student names and their GPAs
	# who have major m
	def get_students_by_major(self,m):
		result = []
		for sname in self._data:
			if self._data[sname].get_major() == m:
				result.append((sname, self._data[sname].gpa()))
		return result

	def get_students_bypass(self):
		result = []
		for sname in self._data:
			result.append((sname, self._data[sname].get_major()))
		return result

	'''
	def get_grades_bypass(self):
		result = []
		grades = self._data.get_course_grades()
		for i in grades:
			name = self.get_name()
			cno = i[0].get_cno()
			grade = i[1]
			result.append(name + ':' + cno + ':' + grade)
		return result
	'''

	# return a list of pairs (sname,major,gpa) of student names, their majors, 
	# and their GPAs who have GPA greater or equal to g
	def get_students_by_gpa(self,g):
		result = []
		for sname in self._data:
			if self._data[sname].gpa() is not None and self._data[sname].gpa() >= float(g):
				result.append((sname, self._data[sname].get_major(), self._data[sname].gpa()))
		return result

	# return String representation of student (see sample run for exact format of string)
	def __str__(self):
		result = ''
		for sname in self._data:
			s = self._data[sname]
			result += str(s) + '\n'
		return result