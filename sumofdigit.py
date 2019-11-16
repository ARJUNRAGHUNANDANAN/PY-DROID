'''Python program to print the sum of digits of a given number
By - Arjun Raghunandanan '''

'''Accepting the Number into the variable NUMBER'''
Number=int(input("Enter a number to find Sum of its Digits :"))
SUM=0

'''loop to perform a Whilw condition which repeatedly Divides the number by 10 and Adds the remainder to the variable SUM'''

while Number>0:
	digit=Number%10
	SUM+=digit
    N=N//10

'''  PrintingSUM  '''	
print("sum of digits of a number=",SUM)

