'''Basic calculator operations using python
Command Line Interface and Menu are in progress'''

print(" modules |  CALCULATOR | INFO |  ")

def arCalc():
    '''  printing Menu for Showning the available operations'''

    print("PYTHON CALCULATOR 2.0  \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
    def add(a,b):
        print( a+b)
    def sub(a,b):
        print(a-b)
    def mul(a,b):
        print(a*b)
    def div(a,b):
        print (a//b)
        
        '''Accepting Input Operators and Operant selection index'''

    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter the Operation Index:  | 1 | 2 | 3 | 4 |    \n"))
    '''if condition ladder executes the selected key index operation'''

    if (c==1):
        add(a,b)
    elif(c==2):
        add(a,b)    
    elif(c==3):
        mul(a,b)
    elif(c==4):
        div(a,b)

'''additional CLI command interface to show details about Calculator program'''

def info():
    print("calculator made using python language by Arjun Raghunandanan")
arCalc()