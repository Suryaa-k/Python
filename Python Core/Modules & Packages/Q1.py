# 1. Write a Python program that attempts to dynamically import a module at 
# runtime. The program should only import the module if it actually exists; 
# otherwise, it should print "Module does not exist".

import importlib
import sys

module_name = input("Enter module name to import: ").strip()

try:
    module = importlib.import_module(module_name)
    print(f"Successfully imported {module_name}")
except ImportError:
    print("Module does not exist")
