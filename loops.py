# Write a program to print multiplication table of a given number using for loop

# num=int(input("Enter a Number"))
# i=1
# while (i<=10):
#     print(num ,"X",i,"=",num*i)
#     i=i+1




# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.





# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for item in l:
#     if item.startswith("S"):
#         print ("The terms with l are " ,item)
 





# 4. Write a program to find whether a given number is prime or not.

# a=int(input("Enter a number to check whether it is prime or not"))
# i=2
# is_prime=True
# while(i<a) :
#     if (a%i ==0):
#         is_prime=False
#         break;
#     i=i+1

# if (is_prime):
#     print(a,"is  a prime number")
# else :
#     print(a,"is not a prime number")











# 5. Write a program to find the sum of first n natural numbers using while loop.

# a=int(input("Enter a number"))
# i=1
# sum=0
# while (i<=a):
#     sum=sum+i
#     i=i+1
# print("The sum of first",a,"Natural no is",sum)
      







# 6. Write a program to calculate the factorial of a given number using for loop.

# a=int(input("Enter a number"))
# i=1
# for j in range (1,a+1) :
#     i=i*j
# print(i)





# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3



# n=3
# a=1
# for i in range (1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("\n")

    

        


# Write a program to print the following star pattern.
# * * *
# *   *        for n = 3
# * * * 

   

n=int(input("Enter a number"))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*"*1,end="")
        print(" "*(n-2),end="")
        print("*"*1,end="")
    print("\n")