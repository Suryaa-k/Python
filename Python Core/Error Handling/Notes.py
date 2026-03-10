# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  ├── GeneratorExit
#  └── Exception
#       ├── ArithmeticError
#       │     ├── FloatingPointError
#       │     ├── OverflowError
#       │     └── ZeroDivisionError
#       │
#       ├── AssertionError
#       │
#       ├── AttributeError
#       │
#       ├── BufferError
#       │
#       ├── EOFError
#       │
#       ├── ImportError
#       │     └── ModuleNotFoundError
#       │
#       ├── LookupError
#       │     ├── IndexError
#       │     └── KeyError
#       │
#       ├── MemoryError
#       │
#       ├── NameError
#       │     └── UnboundLocalError
#       │
#       ├── OSError
#       │     ├── BlockingIOError
#       │     ├── ChildProcessError
#       │     ├── ConnectionError
#       │     │     ├── BrokenPipeError
#       │     │     ├── ConnectionAbortedError
#       │     │     ├── ConnectionRefusedError
#       │     │     └── ConnectionResetError
#       │     ├── FileExistsError
#       │     ├── FileNotFoundError
#       │     ├── InterruptedError
#       │     ├── IsADirectoryError
#       │     ├── NotADirectoryError
#       │     ├── PermissionError
#       │     ├── ProcessLookupError
#       │     └── TimeoutError
#       │
#       ├── ReferenceError
#       │
#       ├── RuntimeError
#       │     ├── NotImplementedError
#       │     └── RecursionError
#       │
#       ├── StopIteration
#       │
#       ├── StopAsyncIteration
#       │
#       ├── SyntaxError
#       │     └── IndentationError
#       │           └── TabError
#       │
#       ├── SystemError
#       │
#       ├── TypeError
#       │
#       ├── ValueError
#       │     └── UnicodeError
#       │           ├── UnicodeDecodeError
#       │           ├── UnicodeEncodeError
#       │           └── UnicodeTranslateError
#       │
#       └── Warning
#             ├── DeprecationWarning
#             ├── PendingDeprecationWarning
#             ├── RuntimeWarning
#             ├── SyntaxWarning
#             ├── UserWarning
#             ├── FutureWarning
#             ├── ImportWarning
#             ├── UnicodeWarning
#             └── ResourceWarning
# try:
#     a=int(input())
#     b=int(input())
#     print(x)
# except ValueError as ve:
#     print(ve)
# except ZeroDivisionError as zd:
#     print(zd)
# except Exception as ex:
#     print("Exception block: ", ex)
# else:
#     print(c)
# finally:
#     print("program complete")
#
#
# def fun(a,b):
#     try:
#         if b<0:
#             raise ValueError("b cannot be negative as per code")
#         print(a+b)
#     except ValueError as ve:
#         print("value Error: ",ve)
#     except ZeroDivisionError as zd:
#         print(zd)
#     except Exception as ex:
#         print("Exception block: ", ex)
# def fun1():
#     print("hello")
#
# a=int(input())
# b=int(input())
# fun(a,b)
# fun1()
# from logging import raiseExceptions

# def fun():
#     try:
#         raise ValueError("b cannot be negative as per code")
#     except ValueError as ve:
#         print(ve)
# def fun2():
#     try:
#         raise ValueError("edho okkati")
#     except ValueError as ve:
#         print(ve)
# fun()
# fun2()
# class PasswordError(Exception):
#     def __init__(self, msg, password):
#         super().__init__(msg)
#         self.password = password
#     # def __str__(self):
#     #     return f'{self.password} is not a valid password, {self.msg}'
#
#
# try:
#     s=input()
#     if len(s)<8:
#         raise PasswordError("b should have 8 chars at least",s)
#
# except PasswordError as pe:
#     print(pe)
#
#     # try
#     # except
#     # else
#     # finally
#     # raise
#     # Custom Error
#     # Custom Exception Class

# class FunctionError(Exception):
#     pass
#
# def fun(a,b):
#     print(a,b)
#     if a > b:
#         raise ArithmeticError("a is greater than b")
# def fun2(a,b):
#     print(a,b)
#     if a < b:
#         raise ValueError("a is less than b")
# def fun3(a):
#     try:
#         a(3,2)#ArithmeticError
#     except ArithmeticError as e:
#         print(e)
#         raise FunctionError(f"Some problem in function {a.__name__}")
#     except ValueError as e:
#         print(e)
#         raise FunctionError(f"Some problem in function {a.__name__}")
# try:
#     fun3(fun)
# except FunctionError as e:
#     print(e)
#