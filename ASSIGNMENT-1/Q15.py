print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")
from collections import namedtuple
from dataclasses import dataclass
EmployeeNT = namedtuple("Employee", ["name", "age", "salary"])
emp1 = EmployeeNT("Alice", 30, 50000)
@dataclass
class EmployeeDC:
    name: str
    age: int
    salary: float
    def give_raise(self, amount):
        self.salary += amount
emp2 = EmployeeDC("Bob", 28, 45000)
emp2.give_raise(5000)
print(f"Named Tuple Employee: {emp1.name}, Age: {emp1.age}, Salary: {emp1.salary}\n")
print(f"Data Class Employee (After Raise): {emp2.name}, Age: {emp2.age}, Salary: {emp2.salary}\n")
print("\nExplanation: Named tuples provide immutable, lightweight data structures for storing values with named fields.\n")
print("Explanation: Data classes are more flexible, allowing default values, type hints, and methods such as give_raise() for modifying data.\n")
print("Explanation: Unlike named tuples, data classes allow mutation of attributes, making them more suitable for objects that require updates.\n")
print("Explanation: Data classes provide built-in methods like __init__, __repr__, and __eq__, reducing boilerplate code and enhancing readability.\n")
