class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.department = department
        
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

class Attendance:
    def __init__(self):
        self.attendance = []
    
    def mark_present(self, date):
        self.attendance.append(date)
        print(f"Marked present for date: {date}")
    
    def total_days(self):
        return len(self.attendance)

class Payroll:
    def __init__(self):
        self.pay_per_day = 1000
    
    def calculate_salary(self, days):
        return self.pay_per_day * days

class EmployeeSystem(Employee, Attendance, Payroll):
    def __init__(self, name, age, emp_id, department):
        Employee.__init__(self, name, age, emp_id, department)
        Attendance.__init__(self)
        Payroll.__init__(self)
    
    def generate_report(self):
        print("\n=== EMPLOYEE REPORT ===")
        self.display_info()
        days = self.total_days()
        salary = self.calculate_salary(days)
        print(f"Days Present: {days}")
        print(f"Total Salary: ${salary}")
        print("====================\n")

if __name__ == "__main__":
    emp1 = EmployeeSystem("Ali", 25, "E001", "IT")
    emp1.mark_present("2025-04-01")
    emp1.mark_present("2025-04-02")
    emp1.generate_report()
    
    emp2 = EmployeeSystem("Waseem", 30, "E002", "HR")
    emp2.mark_present("2025-04-01")
    emp2.generate_report()