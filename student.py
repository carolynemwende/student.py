
class Student :


	def __init__(self,firstname,secondname,age):

			self.firstname= firstname
			self.secondname= secondname
			self.age= age
			

	def fullname(self):
            return "hello {} {}, you are {} yaers old".format(self.firstname,self.secondname,self.age)

	def yob(self):
            return 2019-self.age

	def initials(self):
            a=self.firstname[0]
            b=self.secondname[0]
            c= a+b
            return c
