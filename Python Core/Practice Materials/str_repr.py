# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 
#     def __str__(self):
#         return f"Object of A with {self.x},{self.y}"
#     def __repr__(self):
#         return f"{self.x},{self.y}"
# obj=A(10,20)
# print(obj)
# l=[]
# l.append(obj)
# print(l)

# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 
#     def __add__(self,a2):
#         if isinstance(a2,A):
#             return self.y+a2.x 
#         raise TypeError("Should add same objects")
#     def __radd__(self,o2):
#         return o2.__add__(self)
# obj=A(1,3)
# obj1=A(4,9)
# print(obj+obj1)
# print(obj1+obj)
