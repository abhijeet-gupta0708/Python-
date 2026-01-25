'''1. Create a class (2-D vector) and use it to create another class representing a 3-D
vector.'''

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"The Vectors are {self.i} i and {self.j} j")
# class ThreeDVector (TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
    
#     def show(self):
#         print(f"The Vectors are {self.i} i and {self.j} j and {self.k} k")


# a=ThreeDVector(1,2,3)
# b=TwoDVector(1,2)
# print(b.show())
# a.show()



'''2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
‘Pets’. Add a method ‘bark’ to class ‘Dog'''
    

# class Animals:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"The Animal is {self.name}")

# class Pets(Animals):
#     def __init__(self,name):
#         super().__init__(name)
#     def showpet(self):
        
#         print(f"The Animal  is {self.name} it is a pet")

# class Dog(Pets):
#     def __init__(self,name):
#         super().__init__(name)
#     def bark(self):
#          print(f"Dog is Barking  {self.name}")



# b=Dog("fdsd")
# print(b.show())
# print(b.bark())
# print(b.showpet())



'''3. Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
which changes the value of increment based on the salary.'''
import time
def timer(func):
    def wrapper(*args):
        start=time.time
        result=func(*args)
        end=time.time
        print(f"The function {func.__name__} ran in {end-start}sec")
        return result
    return wrapper

class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment

    
    @property
    @timer
    def salaryAfterIncrement(self):
        print(f"The Salary is ₹ {self.salary} and increment is {self.increment}% and the total salary after increment is ",end=" ")
        return (self.salary + self.salary *(self.increment/100))


a=Employee(250,20)
print(a.salaryAfterIncrement)



''''''