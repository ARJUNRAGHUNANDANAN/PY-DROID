'''  
Python Program to Check whether a given number is an amstrong number or not
By - Arjun Raghunandanan  

Armstrong number is a number that is equal to the sum of cubes of its digits - Google

'''

N=int(input("Enter a Number to check if its a AMSTRONG NUMBER or NOT:")

''' Accepting input to check into a variable N'''

SUM=0
ONE=N

''' Declaring and Initiating sum and Number for Intermediate loop results'''

while N>0:
	digit=n%10
	SUM=SUM+(digit**3)
	N//=10
	
''' Printing the output as "AMSTRONG if ONE and SUM are equal and as "NOT AMSTRONG if ONE and SUM are not equal '''

if (ONE==SUM):
	print("THE NUMBER IS AN AMSTRONG NUMBER") 
else:
	print("THE NUMBER IS NOT AN AMSTRONG NUMBER")
