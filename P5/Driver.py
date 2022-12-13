import sys
from Student import *
from Students import *
from Course import *
from Courses import *

# Open three files, courses.dat, students.dat, and grades.dat, present in directory dname
# Read the data and construct the courses and students objects
# Return the two objects as a pair (see main() for the order)
def load_data(dname):
	# load course data
	cs = Courses()
	with open(dname + "/courses.dat") as f:
		content = f.read().splitlines()
		for line in content:
			x = line.split(':')
			c = Course(x[0], x[1], int(x[2]))
			cs.add_course(c)
	f.close()
	# load student data
	ss = Students()
	with open(dname + '/students.dat') as f:
		content = f.read().splitlines()
		for line in content:
			x = line.split(':')
			s = Student(x[0], x[1])
			ss.add_student(s)
	f.close()

	# load the grades data
	with open(dname + '/grades.dat') as f :
		content = f.read().splitlines()
		for line in content:
			x = line.split(':')
			s = ss.get_student(x[0])
			c = cs.get_course(x[1])
			s.add_course_grade((c, x[2]))
	f.close()
	return cs, ss
	

# Store data from courses and students objects into three files, courses.dat, students.dat, and 
# grades.dat in the folder named dname; Use same format as when you loaded the data
def store_data(courses,students,dname):
	'''
	with open("myfile.dat", "w") as f:
		f.write("This is line 4\n")
		f.write("This is line 5\n")
		f.write("This is line 6\n")
	f.close()
	'''

def main():
	courses,students = load_data(sys.argv[1])
	#print(courses)
	#print(students)
	print("\nWelcome to Grades Database Program\n")
	while True:
		command = input("p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: ").strip()
		if len(command) < 1:
			print("\nInvalid command!\n")
			continue
		elif command[0] == 'p':
			print(students)
		elif command[0] == 's':
			sname = command[2:].strip()
			s = students.get_student(sname)
			if s != None:
				print(s)
			else:
				print("\n"+sname+" NOT FOUND\n")
		elif command[0] == 'm':
			major = command[2:].strip()
			ss = students.get_students_by_major(major)
			print()
			if len(ss) > 0:
				for s in ss:
					print(s[0]+"\t"+str(s[1]))
			else:
				print("NO Students FOUND!")
			print()
		elif command[0] == 'g':
			try:
				gg = float(command[2:].strip())
			except:
				print("\nInvalid GPA Search!\n")
				continue
			ss = students.get_students_by_gpa(gg)
			print()
			if len(ss) > 0:
				for s in ss:
					print(s[0]+"\t"+s[1]+"\t"+str(s[2]))
			else:
				print("NO Students FOUND!")
			print()
		elif command[0] == 'a':
			#a sname:cno:grade
			record = command[2:].strip().split(":")
			if len(record) != 3:
				print("\nInvalid input to add course!\n")
				continue
			student = students.get_student(record[0])
			if student == None:
				print("\nInvalid Student. Cannot add course grade.\n")
				continue
			course = courses.get_course(record[1])
			if course == None:
				print("\nInvalid Course. Cannot add course grade.\n")
				continue
			if record[2].upper() not in ['A','B','C','D','F']:
				print("\nInvalid Grade. Cannot change course grade.\n")
				continue
			else:
				student.add_course_grade((course,record[2].upper()))
				print("\n",record," ADDED\n")
		elif command[0] == 'c':
			#c sname:cno:grade
			record = command[2:].strip().split(":")
			if len(record) != 3:
				print("\nInvalid input to change course grade!\n")
				continue
			student = students.get_student(record[0])
			if student == None:
				print("\nInvalid Student. Cannot change course grade.\n")
				continue
			if student.takes_course(record[1]):
				if record[2].upper() in ['A','B','C','D','F']:
					student.update_course_grade(record[1],record[2])
					print("\nGRADE CHANGED\n")
				else:
					print("\nInvalid Grade. Cannot change course grade.\n")
					continue
			else:
				print("\nInvalid Course. Cannot change course grade.\n")
				continue
			print()
		elif command[0] == 'q':
			break
		else:
			print("\nInvalid command\n")
	store_data(courses,students,sys.argv[1])
	print("\nBye!\n")

main()