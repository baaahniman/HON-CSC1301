class Student:

	# constructor
	def __init__(self,name,major):
		self._name = name
		self._major = major
		self._course_grades = []	# list of pairs (course,grade)

	# getter
	def get_name(self):
		return self._name

	# getter
	def	get_major(self):
		return self._major

	# getter
	def get_course_grades(self):
		return self._course_grades

	# setter
	def set_major(self,major):
		self._major = major

	# setter
	def set_course_grades(self,grades):
		self._course_grades

	# return True if student takes course numbered cno; False otherwise
	def takes_course(self,cno):
		for i in self._course_grades:
			if cno == i[0].get_cno():
				return True
		return False

	# return GPA for student (rounded to 2 decimal places)
	def gpa(self):
		sum = 0
		n = 0
		d = {
			'A': 4,
			'B': 3,
			'C': 2,
			'D': 1,
			'F': 0
		}
		for i in self._course_grades:
			sum += d[i[1]] * i[0].get_credits()
			n += i[0].get_credits()
		if n > 0:
			return round(sum / n, 2)
		else:
			return None

	# add pair cg = (course,grade) to course_grades
	def add_course_grade(self,cg):
		self._course_grades.append(cg)

	# update grade for course with number cno; new grade is gr
	def update_course_grade(self,cno,gr):
		temp = []
		for i in self._course_grades:
			if cno == i[0].get_cno():
				temp.append((i[0], gr))
			else:
				temp.append(i)
		self._course_grades = temp

	# return string representation of student
	# see sample run for exact format to display student object
	def __str__(self):
		result = 'Name: ' + self._name + '\n'
		result += 'Major: ' + self._major + '\n'
		for i in self._course_grades:
			result += str(i[0]) + ' GRADE = ' + i[1] + '\n'
		result += 'GPA: ' + str(self.gpa()) + '\n'
		return result

	'''
	Name: Blake
	Major: CSC
	CSC1301:Principles of Computer Science I:4 GRADE = B
	CSC1302:Principles of Computer Science II:4 GRADE = B
	CSC2720:Data Structures:3 GRADE = B
	CSC3320:Systems Level Programming:3 GRADE = B
	GPA: 3.0
	'''