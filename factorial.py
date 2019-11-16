'''  Python program to print the factorial of a given number
By - Arjun Raghunandanan 
Factorial of a number is the product of an integer and all the integers below it  '''


n=int(input("enter a number"))
'''  accepting input n as the number for which the factorial is to be found  '''
fact=1
for i in range (2,n+1):
	fact=fact*i
'''  recurring loop which returns the factorial of that number  '''

print("factorial of the number is  : ",fact)
'''printing the result'''
