class Employee:
    companyName = "Apple"   # Class Variable
    noOfEmployees = 0    # Class Variable

    def __init__(self, name):
        self.name = name    # Instance Variable
        self.raise_amount = 0.02    # Instance Variable
        Employee.noOfEmployees += 1   # Class Variable is incremented so as to count no of employees

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")


# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()
