'''1. Write a program using functions to find greatest of three numbers.'''


# def greatest (num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         great=num1
#     elif(num2>num1 and num2>num3):
#         great=num2
#     else:
#         great=num3
#     print(great);

# num1=int(input("ENter a number"))
# num3=int(input("ENter a number"))
# num2=int(input("ENter a number"))
# greatest(num1,num2,num3)




'''2. Write a python program using function to convert Celsius to Fahrenheit.'''

# def temp(cel):
#     print((cel*(9/5))+32)
# temp(int(input("Enter ")))



'How do you prevent a python print() function to print a new line at the end'

# print("this is end",end="")
# print("this is end",end="")






'''4. Write a recursive function to calculate the sum of first n natural numbers.'''

# def sum(n):
#     if(n==1):
#         return 1
#     else:
        
#         return n+sum((n-1));

# print(sum(int(input("E"))))






'''Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

# def pat(n):
#     for i in range (n,0,-1):
#         for j in range (0,i):
#             print("*",end="")
#         print("\n")


# n=int(input("E"))
# pat(n)
    
    


'''Write a python function which converts inches to cms'''

def con(inches):
    print(inches*2.4);

n=int(input("E"));
con(n)
