# Prgm 01
# x=100
# def fun(a,b,c=10):
#     print(a+b+c)
#     print(x)
#     x=200
#     return((a+b+c)%x)
# fun(100,100,-20)
# print(fun(a=100,b=20)) # Error Cmg 

#Prgm 02
# def fun(*x):
#     l=list(x) 
#     for i in x:
#         print(i)
# fun(1,2,3,3.0,"Hello",True)

#Prgm 03
# def fun(x):
#     def y(z):
#         print(z)
#     return y
# x=fun(100)
# x(100) #100

#prgm 04
# def fun(y):
#     print(y(20))
# def fun1(x):
#     return x*2
# fun(fun1)

#Prgm 05
# l=[1,2,3,4,5,6]
# print(list(map(lambda x:x**2,l)))
# print(list(filter(lambda x: True if x%2==0 else False,l)))
# import functools
# print(functools.reduce(lambda a,b:a*b,l))

# class A:
#     x=10
#     def __init__(self,y):
#         self.y=y
#         A.x+=1
#     def m1(self):
#         print(self.x,self.y)
#     @classmethod
#     def m2(cls):
#         print(cls.x,cls.y)
#     @staticmethod
#     def m3(z):
#         print(z+A.x)
# obj=A(20)
# obj.m1()
# obj.m2()
# obj.m3(90)
# A.m1()
# A.m2()
# A.m3(90)

#Q1 
# class Book:
#     tb=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         Book.tb+=1
#     @classmethod
#     def m1(cls,bs):
#         t,a=bs.split("-")
#         return cls(t,a)
#     def pname(self):
#         print(self.title)
#     @staticmethod
#     def prating(rat):
#         print(rat)

# b1=Book("Hi","Hello")
# b2=Book.m1("H-Hello")
# b1.pname()
# b2.pname()  
# print(Book.tb) 