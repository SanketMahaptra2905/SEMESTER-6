print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

num1 = Complex(3, 4)
num2 = Complex(1, 2)
result = num1 + num2

print(f"First Complex Number: {num1}")
print(f"Second Complex Number: {num2}")
print(f"Sum of Complex Numbers: {result}")

print("\nExplanation: Operator overloading allows customizing the behavior of built-in operators like '+'.\n")
print("Explanation: The __add__ method is overridden in the Complex class to add real and imaginary parts separately.\n")
print("Explanation: When two Complex objects are added using '+', Python automatically calls the __add__ method to perform the addition.\n")
print("Explanation: This demonstrates polymorphism and enhances code readability by allowing intuitive mathematical operations on custom objects.\n")
