'''python calculator by ARJUN RAGHUNANDANAN '''


print "PROGRAM FOR CALCULATOR\n"

while True:
    y=input("Enter First number")
    z=input("Enter Second Number")

    x=input("Enter your operation \n 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION \n")
    
    if (x==1):
        print z+y
    elif (x==2):
        print y-z
    elif (x==3):
        print y*z
    elif (x==4):
        print y//z
    else:
        exit(0)
