# class Company:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         return self.name*2

# class Employee:
#     def __init__(self,myname):
#         self.agg_name=myname
        
#     def check(self):
#         return self.agg_name.show()
        


# com=Company('Shreya LTD')
# emp1=Employee(com)
# # print(emp1.__project)
# print(emp1.check())
# class Parent:
    
#     def __init__(self,name):
#         print(name,"is derived from another class")
    
#     def f1(self):
#         print('Function of parent class')

# class Child(Parent):
#     def __init__(self, name):
#         print(name,'is a subclass')
#         super().__init__(name)
#         self.f1()

#     def f1(self):
#         super().f1()
#         print('Function of child class')

# obj=Child('Child')
# Code to demonstrate Composition 

# Class Salary in which we are 
# declaring a public method annual salary 
# class Salary: 
# 	def __init__(self, pay, bonus): 
# 		self.pay = pay 
# 		self.bonus = bonus 

# 	def annual_salary(self): 
# 		return (self.pay*12)+self.bonus 


# # Class EmployeeOne which does not 
# # inherit the class Salary yet we will 
# # use the method annual salary using 
# # Composition 
# class EmployeeOne: 
# 	def __init__(self, name, age, pay, bonus): 
# 		self.name = name 
# 		self.age = age 

# 		# Making an object in which we are 
# 		# calling the Salary class 
# 		# with proper arguments. 
# 		self.obj_salary = Salary(pay, bonus) # composition 

# 	# Method which calculates the total salary 
# 	# with the help of annual_salary() method 
# 	# declared in the Salary class 
# 	def total_sal(self): 
# 		return self.obj_salary.annual_salary() 

# # Making an object of the class EmployeeOne 
# # and providing necessary arguments 
# emp = EmployeeOne('Geek', 25, 10000, 1500) 

# # calling the total_sal method using 
# # the emp object 
# print(emp.total_sal()) 

# Code to demonstrate Aggregation 

# Salary class with the public method 
# annual_salary() 
# class Salary: 
# 	def __init__(self, pay, bonus): 
# 		self.pay = pay 
# 		self.bonus = bonus 

# 	def annual_salary(self): 
# 		return (self.pay*12)+self.bonus 


# # EmployeeOne class with public method 
# # total_sal() 
# class EmployeeOne: 

# 	# Here the salary parameter reflects 
# 	# upon the object of Salary class we 
# 	# will pass as parameter later 
# 	def __init__(self, name, age, sal): 
# 		self.name = name 
# 		self.age = age 

# 		# initializing the sal parameter 
# 		self.agg_salary = sal # Aggregation 

# 	def total_sal(self): 
# 		return self.agg_salary.total_salary()

# # Here we are creating an object 
# # of the Salary class 
# # in which we are passing the 
# # required parameters 
# salary = Salary(10000, 1500) 

# # Now we are passing the same 
# # salary object we created 
# # earlier as a parameter to 
# # EmployeeOne class 
# emp = EmployeeOne('Geek', 25, salary) 

# print(emp.total_sal()) 

from abc import ABC,abstractmethod
class Fruit(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        self.intro()
    
    def intro(self):
        print("This is for eating!!")
    
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def taste(self):
        pass

class Mango(Fruit):
    def name(self):
        "This is a mango"
    def taste(self):
        "Sweet"


man=Mango()


