#Problem ::1   Write a program to find the greatest of four numbers entered by the user


# a=int(input("Enter a  Number  "))
# b=int(input("Enter a  Number  "))
# c=int(input("Enter a  Number  "))
# d=int(input("Enter a  Number  "))
# if (a>b and a>c and a>d):
#  print(a," is greaterst")
# if(b>a and b>c and b>d):
#  print(b,"is greatest ")
# if(c>a and c>b and c>d):
#  print(c,"is greatest ")
# if(d>a and d>b and d>c):
#  print(d,"is greatest ")

#SHORTER METHOD

# a=int(input("Enter a  Number  "))
# b=int(input("Enter a  Number  "))
# c=int(input("Enter a  Number  "))
# d=int(input("Enter a  Number  "))
# print("The max value is",max(a,b,c,d))



# #Problem 2::
#                     Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


# marks1=int(input("Enter 1st subject marks"))
# marks2=int(input("Enter 2nd subject marks"))
# marks3=int(input("Enter 3rd subject marks"))
# if(marks1<33 or marks2<33 or marks3<33) :
#     print("You Failed")
# if(((marks1+marks2+marks3)/3)<40) :
#     print("You Failed You got only",((marks1+marks2+marks3)/3))
# else :
#     print("You Passed and got ",((marks1+marks2+marks3)/3))