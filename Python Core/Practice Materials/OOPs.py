# class A:
#     __x=20
#     @property
#     @classmethod
#     def y(cls):
#         return cls.__x
# print(A.y)
# class B:
#     def __init__(self,x):
#         self.__x=x
#     @property
#     def y(self):
#         return self.__x
#     @y.setter
#     def y(self,z):
#         self.__x=z

# from abc import ABC, abstractmethod
# class A(ABC):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def m1(self):
#         print("Inside Abctract Class")
#     @abstractmethod
#     def m2(self):
#         pass
#