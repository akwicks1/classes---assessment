"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

	1. Abstraction - you only need to show the necessary details
	2. Encapsulation - keeps everything together
	3. Polymorphism - the ability to interchange parts 

2. What is a class?
	is a type of thing that allows you to structure your code in a clean and consistent way

3. What is an instance attribute?
	an attribute(or characteristic) that belongs to a particular instance-the post on itself first then the parent

4. What is a method?
	a method is like a function defined on a class that always have at least one parameter - self.

5. What is an instance in object orientation?
	it's an object of the class that has all of the attributes as described in the class definition.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
	a class attribute is a characteristic of all instances in the class.  An instance attribute can 
	override the class attribute.  An instance looks to itself to see if they have an attribute and 
	if they don't they look at the parent.


"""


# Parts 2 through 5:
# # Create your classes and class methods
# 	"""Set first name, last name and address as instance
# 		attributes of the class Student.
# 		"""

class Student(object):
	"""A student."""

	def __init__(self, first_name, last_name, address):
		"""Initializing a student."""

		self.first_name = first_name
		self.last_name = last_name
		self.address = address


# 	def speak(self):
# 		"""The person speaks."""
# 		print "Hi {} {}".format(self.first_name, self.last_name)

# 	def live(self):
# 		"""Where the person lives."""
# 		print "I live at {}".format(self.address)

# 	def __repr__(self):
# 		print "This is how the repr method works {}".format(self.first_name)

# abby = Student("Abby", 'Wicks', '814')
# abby.speak()
# abby.live()
# abby.__repr__()

# Long story short, calling repr on an object should return 
# a string s such that calling eval(s) will re-create that object. 

class Question(object):
	"""A question with the correct answer."""

	def __init__(self, question, answer):
		"""Initializing a question with the answer."""

		self.question = question
		self.answer = answer

	# def ask_question(self):
	# 	print "The question is {}".format(self.question)

	# def correct_answer(self):
	# 	print "The answer to the question is {}".format(self.answer)

	def ask_and_evaluate(self):
		"""Ask user the question and if the user supplies the correct answer return True."""
		print self.question
		user_answer = raw_input("")
		if user_answer == self.answer:
			return True
		# 	print True
		# else:
		# 	print False

dog_question = Question("Who is the cutest puppy?", "Honey")
wa_capital = Question("What is the capital of Washington state?", "Olympia")
python_author = Question("Who is the author of python?", "Guido Van Rossum")
hb_mascot = Question("Who is Hackbright's mascot?", "Baloonicorn")

class Exam(object):
	"""An Exam."""

	def __init__(self, name):
		"""Initializing an exam and the name of the exam."""

		self.name = name
		self.questions = []

	def add_question(self, question):

		questions = self.questions.append(question) 

	def administer(self):

		answers_correct = 0

		for question in self.questions:
			if question.ask_and_evaluate() is True:
				answers_correct += 1



		return answers_correct
		# answers_correct = 0
		# num_of_questions = 0
		# num_of_correct = 0.0
		# for question in self.questions:
		# 	print question
		# 	user_answer = raw_input("")
		# 	if user_answer == answer:
		# 		answers_correct += 1
		# 		num_of_questions += 1
		# 	else:
		# 		num_of_questions += 1
		# num_of_correct = answers_correct / num_of_questions
		# print num_of_correct

	#TODO figure out how to get the decimal percentage

class StudentExam(object):
	"""Create an exam for a student."""

	def __init__(self, student, exam, score):
		"""Initializing an exam for a student, showing their score."""

		self.student = student
		self.exam = exam
		self.score = score

	def take_test(self):
		self.score = exam.administer()
		print self.score


class Quiz(Exam):

	def give_quiz(self):
		pass