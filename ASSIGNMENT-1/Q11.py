print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")

class Dog:
    def speak(self):
        return "Woof! Woof!"

class Robot:
    def speak(self):
        return "Beep! I am a robot."

def describe(entity):
    print(entity.speak())

dog = Dog()
robot = Robot()

describe(dog)
describe(robot)

print("\nExplanation: Duck typing in Python means that an object's suitability for use is determined by the presence of certain methods, rather than its specific type.\n")
print("Explanation: In this example, both Dog and Robot classes have a speak() method, so they can be passed to the describe() function without checking their type.\n")
print("Explanation: The describe() function works as long as the passed object has a speak() method, demonstrating the flexibility and dynamic nature of Python's typing system.\n")
print("Explanation: This concept follows the principle: 'If it looks like a duck and quacks like a duck, it must be a duck,' allowing polymorphic behavior without explicit inheritance.\n")
