### Type Hint/Annotation with Checking examples
""" 
List is imported since I am using python 3.7 - 3.9+ includes a list type already 
Type hinting or type annotation is important to ensure the type that is passed to a function arguments is correct. 
Python is dynamically typed and this can cause issues where the type of a variable is overwritten or changed in a program. 
Type checking helps validate the correct types. Mypy can check the types of functions with type hinting included. 
To begin using type checking: pip install mypy
Run type checker by: mypy type_hinting.py  
Can you find the issue present in this file?
"""
from typing import List

person = "Eleven"
person_fake = "11"
### No type hinting.
def hello_world(name):
    return "Hello " + name


### type hint to accept and return str
def hello_world_type(name: str) -> str:
    if name.isnumeric():
        return None
    else:
        return "Hello " + name


print(hello_world(person))

print(hello_world_type(person))

print(hello_world_type(person_fake))

### type hint take a int and return a list
def list_gen(n: int) -> List[int]:
    new_list = []
    for i in range(n):
        new_list.append(i)
    return new_list


print(list_gen(5))