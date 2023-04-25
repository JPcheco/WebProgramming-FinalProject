import sys
from user import User

class UserDao:
	def __init__(self):
		self.filename = "users.txt"
		
	def readUsers(self):
		result = []
		with open(self.filename, 'r') as file:
			# read the file into lines
			lines = file.readlines() 

			# iterate through lines, splitting each line into strings
			for line in lines:
				strings = (line.rstrip('\n')).split()
				#print(strings, file = sys.stderr)
				userid = strings[0]
				password = strings[1]
				user = User(userid,password)
				
				result.append(user)

		return result
	
	def selectAll(self):
		result = self.readUsers()
		return result

	def getUsers(self):
		result = []
		with open(self.filename,'r') as file:
			lines = file.readlines()

			for line in lines:
				row = line.strip('\n').split(' ')
				ans = row[0]
				result.append(ans)

		return result
	
	def selectByUserId(self,userid):
		users = self.selectAll()
		
		for user in users:
			if (user.userid == userid):
				return user
		
		return None
		
	def insert(self,new_userid, new_password):
		info = new_userid + " " + new_password
		with open(self.filename, 'a') as file:
			file.write(info + '\n')