print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")

class CommissionEmployee:
    def __init__(self, name, employee_id, sales_amount, commission_rate):
        if sales_amount < 0 or commission_rate < 0:
            raise ValueError("Sales amount and commission rate cannot be negative.")
        self.name = name
        self.employee_id = employee_id
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def earnings(self):
        return self.sales_amount * self.commission_rate

    def __repr__(self):
        return f"CommissionEmployee(Name: {self.name}, ID: {self.employee_id}, Sales: {self.sales_amount}, Commission Rate: {self.commission_rate})"

    def update_sales(self, new_sales):
        if new_sales < 0:
            raise ValueError("Sales amount cannot be negative.")
        self.sales_amount = new_sales

employee = CommissionEmployee("John Doe", 101, 5000, 0.10)
print(employee)
print(f"Earnings: {employee.earnings()}")

try:
    employee.update_sales(7000)
    print(f"Updated Earnings: {employee.earnings()}")
except ValueError as e:
    print(f"Error: {e}")

try:
    employee.update_sales(-3000)
except ValueError as e:
    print(f"Error: {e}")

print("\nExplanation: The CommissionEmployee class includes attributes for personal details and sales data, ensuring that sales and commission rate cannot be negative.\n")
print("Explanation: The earnings() method calculates commission-based earnings, and update_sales() allows modification with validation to prevent negative values.\n")
print("Explanation: The __repr__ method provides a clear representation of the object for debugging and display purposes.\n")
print("Explanation: This approach ensures data security, prevents incorrect modifications, and demonstrates good object-oriented design practices.\n")
