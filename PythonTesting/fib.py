#This is a comment
#Program to print fibinacci numbers

num1 = 0
num2 = 1

numRuns = int(input("How many numbers do you want?"))

for x in range(0, numRuns):
	print (num1)
	temp = num1
	num1 = num2
	num2 = temp + num1 #equivalent from old num1 + old num2
	
