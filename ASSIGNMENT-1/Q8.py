print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Number of Doors: {self.num_doors}")

vehicle = Vehicle("Toyota", "Camry")
car = Car("Honda", "Civic", 4)

vehicle.display_info()
car.display_info()

print("\nExplanation: The Car class inherits from the Vehicle class, meaning it automatically gets the attributes and methods of Vehicle.\n")
print("Explanation: The Car class extends the functionality by adding an additional attribute, num_doors, and modifying the display_info() method to include this attribute.\n")
print("Explanation: The super().__init__(make, model) in the Car class calls the constructor of the Vehicle class, ensuring that the base attributes are properly initialized.\n")
print("Explanation: This demonstrates object-oriented programming principles such as inheritance and method overriding, allowing for code reuse and extension of functionality.\n")
