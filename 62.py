# Private Access Modifier

class Employee:
    def __init__(self):
        self.__name = "Harry"


emp = Employee()
# print(emp.__name) # Cannot be accessed directly
print(emp._Employee__name)  # Can be accessed indirectly

print(emp.__dir__())    # Shows operations that can be performed on the object
