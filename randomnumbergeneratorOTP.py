'''PROGRAM 3  RANDOM NUM  '''

import random
'''
Generating a random OTP by using Python random number library'''

a=random.randint(100,999)

print a

'''
PROCEDURE TO SENT OTP TO USER

'''  
OTP=input("Enter your OTP \n ")
if OTP==a:
    print("OTP VERIFICATION IS SUCCESFUL")
else:
    print("OTP NOT VERIFIED Please check OTP")
