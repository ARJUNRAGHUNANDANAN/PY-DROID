'''Python program to check if a number is PALINDROME or NOT 
by- Arjun Raghunandanan  '''

N=int(input("Enter a number to check if it is a PALINDROME or NOT:"))

reverse=0
n1=N
while   N>0:
	digit=N%10
	reverse=(reverse*10)+digit
	N//=10
print("reverse=",reverse)
if(n1==reverse):
	print("THE NUMBER IS PALINDROME")
else:
	print("THE NUMBER IS NOT PALINDROME")
	

