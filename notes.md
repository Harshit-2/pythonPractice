REPL => Read Evaluate Print Loop

Question -> Emulate do while loop in Python

Answer->

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
       break


# String Methods-

i)     upper() :
       The upper() method converts a string to upper case.

ii)    lower()
       The lower() method converts a string to lower case.

iii)   strip() :
       The strip() method removes any white spaces before and after the string.

iv)    rstrip() :
       The rstrip() removes any trailing characters.

v)     replace() :
       The replace() method replaces all occurences of a string with another string.

vi)    split() :
       The split() method splits the given string at the specified instance and returns the separated strings as list items.

vii)   capitalize() :
       The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

viii)  center() :
       The center() method aligns the string to the center as per the parameters given by the user.

ix)    count() :
       The count() method returns the number of times the given value has occurred within the given string.

x)     endswith() :
       The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

xi)    find() :
       The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

xii)   index() :
       The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

       As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

xiii)  isalnum() :
       The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

xiv)   isalpha() :
       The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

xv)    islower() :
       The islower() method returns True if all the characters in the string are lower case, else it returns False.

xvi)   isprintable() :
       The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

xvii)  isspace() :
       The isspace() method returns True only and only if the string contains white spaces, else returns False.

xix)   istitle() :
       The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

xx)    isupper() :
       The isupper() method returns True if all the characters in the string are upper case, else it returns False.

xxi)   startswith() :
       The startswith() method checks if the string starts with a given value. If yes then return True, else return False.

xxii)  swapcase() :
       The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

xxiii) title() :
       The title() method capitalizes each letter of the word within the string.


# There are four types of arguments that we can provide in a function:

 •  Default Arguments
 •  Keyword Arguments
 •  Variable length Arguments
 •  Required Arguments

Default Arguments - 

We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Keyword Arguments - 

We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Variable length Arguments - 

Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

# There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Keyword Arbitrary Arguments:
While creating a function, pass a ** before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Required Arguments - 

In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.


Range of Index-

You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.


# Lists

• Lists are ordered collection of data items.
• They store multiple items in a single variable.
• List items are separated by commas and enclosed within square brackets [].
• Lists are changeable meaning we can alter them after creation.

# List Methods-

i)   list.sort()
     This method sorts the list in ascending order. The original list is updated

ii)  reverse()
     This method reverses the order of the list.

ii)  index()
     This method returns the index of the first occurrence of the list item.

iii) count()
     Returns the count of the number of items with the given value.

iv)  copy()
     Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

v)   append():
     This method appends items to the end of the existing list.

vi)  insert():
     This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

vii) extend():
     This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.


# Tuples

• Tuples are ordered collection of data items.
• They store multiple items in a single variable.
• Tuple items are separated by commas and enclosed within round brackets ().
• Tuples are unchangeable meaning we can not alter them after creation.

To create tuple with one element, we need to add a comma after the element. If we don't add a comma, then the interpreter will consider it as an int.
i.e. tuple = (1,)

# Tuple Methods-

i)  count():
    The count() method of Tuple returns the number of times the given element appears in the tuple.

ii) index() method
    The Index() method returns the first occurrence of the given element from the tuple.


# Sets

• Sets are unordered collection of data items.
• They store multiple items in a single variable.
• Set items are separated by commas and enclosed within curly brackets {}.
• Sets are unchangeable, meaning you cannot change items of the set once created.
• Sets do not contain duplicate items.

To create an empty set, we need to use set() method. If we use {} to create an empty set, then the interpreter will consider it as a dictionary.
i.e. exampleSet = set()

# Set Methods-

i)    union() and update():
      The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

ii)   intersection and intersection_update():
      The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

iii)  symmetric_difference and symmetric_difference_update():
      The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

iv)   difference and difference_update():
      The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

v)    isdisjoint():
      The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

vi)   issuperset():
      The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

vii)  issubset():
      The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

viii) add()
      If you want to add a single item to the set use the add() method.

ix)   update()
      If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

x)    remove()/discard()
      We can use remove() and discard() methods to remove items form list.
      The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

xi)   pop()
      This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

xii)  del
      del is not a method, rather it is a keyword which deletes the set entirely.

xiii) clear():
      This method clears all items in the set and prints an empty set.


# Dictioneries-

• Dictionaries are ordered collection of data items. 
• They store multiple items in a single variable. 
• Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# Dictionary Methods-

i)   update()
     The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

ii)  clear():
     The clear() method removes all the items from the list.

iii) pop():
     The pop() method removes the key-value pair whose key is passed as a parameter.

iv)  popitem():
     The popitem() method removes the last key-value pair from the dictionary.

v)   del:
     We can also use the del keyword to remove a dictionary item. If key is not provided, then the del keyword will delete the dictionary entirely.


# For loop with else-

Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.


# Enumerate function-

The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.


# Virtual Environment-

A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.
To create a virtual environment in Python, you can use the venv module that comes with Python. 

    1)  python -m venv myenv               # Create virtual environment named myenv

    2)  source/myenv/bin/activate          # To activate virtual environment in linux/macOS

    3)  myenv\Scripts\activate.bat         # To activate virtual environment in windows

    4)  myenv\Scripts\activate.ps1         # To activate virtual environment in windows in powershell

    5)  pip install pandas                 # To install pandas

    6)  pip install pandas==1.4.4           # To install specific version of pandas in virtual environment

    7)  import pandas as pd                # To import pandas in python

    8)  pd.__version__                     # To check version of pandas

    9)  deactivate                         # To deactivate virtual environment

    10)  pip freeze                        # To check all the packages installed in virtual environment

    11)  pip freeze > requirements.txt     # To save all the packages installed in virtual environment in requirements.txt file

    12)  pip install -r requirements.txt   # To install all the packages from requirements.txt file


# How importing in python works-

Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.
To import a module in Python, you use the import statement followed by the name of the module.


# The if __name__ == "__main__"

The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.


★ Clink:     
       Opening a file in read mode will raise an error if the file is not found but if file is opened in write or append mode it will create that file if the file is not there


# seek() function-

The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position.

# tell() function-

The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position.

# truncate() function-

When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.


# lambda function-

In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

lambda arguments: expression

Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.


# map-

       The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

       map(function, iterable)

       The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# filter-

       The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

       filter(predicate, iterable)

       The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# reduce-

       The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

       reduce(function, iterable)

       The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

       The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.


# 'is' vs '==' in Python-

In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

is --> Exact location of object in memory
== --> Value


# self parameter-

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.


# Constructors-

A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

Types of Constructors in Python-

1) Parameterized Constructor
2) Default Constructor

Parameterized Constructor in Python:
When the constructor accepts arguments along with self, it is known as parameterized constructor.
These arguments can be used inside the class to assign the values to the data members.

Default Constructor in Python:
When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.


# Python Decorators -

Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

@decorator_function
def my_function():
    pass

✯ Conclusion-
       Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

       In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.


# Getters-

Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator.
To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute.


# Setters-

It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

✯ In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.


# Inheritance in python-

When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

Types of inheritance:
1) Single inheritance
2) Multiple inheritance
3) Multilevel inheritance
4) Hierarchical Inheritance
5) Hybrid Inheritance

1) Single Inheritance:
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

2) Multiple Inheritance:
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

3) Multilevel Inheritance :
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

4) Hierarchical Inheritance:
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.

5) Hybrid Inheritance:
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.


# Access Specifiers/Modifiers-

Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Public Access Specifier in Python -

All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

Private Access Modifier -

By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.


# Name mangling - 

Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

Protected Access Modifier - 

In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.


# Static Method - 

Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.


# Instance vs class variables -

In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

Class Variables:
Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.

Instance Variables:
Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.

Summary:
In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance.

It's also worth noting that, in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable. They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name. But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.


# What are Python Class Methods?

A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

Conclusion:
Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.


# Class Methods as Alternative Constructors -

In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary.


# dir(), __dict__ and help() methods

We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), __dict__, and help(). 

The dir() method:
dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.

The __dict__ attribute:
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.

The help() mehthod:
help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.


# Super keyword in Python - 

The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.


# Magic/Dunder Methods in Python - 

These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour. Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

__init__ method:
The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already

__str__ and __repr__ methods:
The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

__len__ method:
The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.

__call__ method:
The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.


# Method Overriding - 

Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

In Python, method overriding is a way to customize the behavior of a class based on its specific needs. In this base class, the area method is defined, but does not have any implementation. If you want to create a derived class that represents a circle, you can override the area method and provide an implementation.

It's important to note that when you override a method, the new implementation must have the same method signature as the original method. This means that the number and type of arguments, as well as the return type, must be the same.

Another way to customize the behavior of a class is to call the base class method from the derived class method. To do this, you can use the super function. The super function allows you to call the base class method from the derived class method, and can be useful when you want to extend the behavior of the base class method, rather than replace it.


# Operator Overloading -

Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

Conclusion:
Operator overloading is a powerful feature in Python that allows you to create more readable and intuitive code. By redefining the behavior of mathematical and comparison operators for custom data types, you can write code that is both concise and expressive. However, it's important to use operator overloading wisely, as overloading the wrong operator or using it inappropriately can lead to confusing or unexpected behavior.


# Single Inheritance in Python -

Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.


# Multiple Inheritance -

Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.


# MRO-

The method resolution order (MRO) is the order in which Python looks for a method in a hierarchy of classes. It is used to determine the order in which methods are inherited in multiple inheritance. The MRO is a property of a class, and can be accessed using the mro() method.


# Multilevel Inheritance -

Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.

Another important aspect of multilevel inheritance is that it allows you to reuse code and avoid repeating the same logic multiple times. This can lead to better maintainability and readability of your code, as you can abstract away complex logic into base classes and build upon them.

In conclusion, multilevel inheritance is a powerful feature in object-oriented programming that allows you to create complex and intricate classes by building upon existing ones. It provides the benefits of code reuse, maintainability, and readability, while also requiring careful consideration to avoid potential problems.


# Hybrid Inheritance -

Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

In this way, hybrid inheritance allows for a flexible and powerful way to inherit attributes and behaviors from multiple classes in a hierarchy or chain.


# Hierarchical Inheritance -

Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.

In conclusion, hierarchical inheritance is a way of establishing relationships between classes in a hierarchical manner. It allows multiple subclasses to inherit from a single base class, which helps in code reuse and organization of code in a more structured manner.


# The time Module in Python -

The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.

time.time()
The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time.

time.sleep()
The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.

time.strftime()
The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report.

Conclusion
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. Whether you are writing a script, a library, or an application, the time module is a powerful tool that can help you perform time-related tasks with ease and efficiency. So, if you haven't already, be sure to check out the time module in Python and see how it can help you write better, more efficient code.


# Creating Command Line Utilities -

Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python, you can create your own command line utilities using the built-in argparse module.

Syntax 1:

    import argparse

    parser = argparse.ArgumentParser()

    # Add command line arguments
    parser.add_argument("arg1", help="description of argument 1")
    parser.add_argument("arg2", help="description of argument 2")

    # Parse the arguments
    args = parser.parse_args()

    # Use the arguments in your code
    print(args.arg1)
    print(args.arg2)
    
Syntax 2: Adding optional arguments

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
    args = parser.parse_args()

    print(args.optional)
    
Syntax 3: Adding positional arguments

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("positional", help="description of positional argument")
    args = parser.parse_args()

    print(args.positional)

Syntax 4: Adding arguments with type

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="description of integer argument")
    args = parser.parse_args()

    print(args.n)


# The Walrus Operator -

The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.


# Shutil Module -

Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. In this repl, we'll take a closer look at the shutil module and its various functions and how they can be used in Python.

• shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

• shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

• shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

• shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

• shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.


# Generators -

Generators in Python are special type of functions that allow you to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

# Creating a Generator -

In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.
The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.

Benefits of Generators -

Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once.

Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.

Conclusion -

Generators in Python are a powerful tool for working with large or complex data sets, allowing you to generate the values on-the-fly and store only what you need in memory. Whether you are working with a large dataset, performing complex calculations, or generating a sequence of values, generators are a must-have tool in your programming toolkit.


# Function Caching -

Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called.

Benefits of Function Caching -

Function caching can have a significant impact on the performance of a program, particularly for computationally expensive functions. By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources.

Another benefit of function caching is that it can simplify the code of a program by removing the need to manually cache the results of a function. With the functools.lru_cache decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.

Conclusion -

Function caching is a technique for improving the performance of a program by storing the results of a function so that you can reuse the results instead of recomputing them every time the function is called. In Python 3, function caching can be achieved using the functools.lru_cache decorator, which provides an easy and efficient way to cache the results of a function. Whether you're writing a computationally expensive program, or just want to simplify your code, function caching is a great technique to have in your toolbox.


# Regular Expressions in Python -

Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

Metacharacters in regular expressions -

[]  Represent a character class
^   Matches the beginning
$   Matches the end$
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters separated by it.)
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE to match.
()  Enclose a group of REs

Find list of more meta characters here -
https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

https://regexr.com/

re.search() -

re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.

re.findall() -

You can also use the re.findall function to find all occurrences of the pattern in a string


# Async IO in Python -

Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

# Multithreading in Python -

Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading.

Creating a thread -

To create a thread, we need to create a Thread object and then call its start() method. The start() method runs the thread and then to stop the execution, we use the join() method.

Functions-

The following are some of the most commonly used functions in the threading module:

• threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.

• threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.

Creating multiple threads -

Creating multiple threads is a common approach to using multithreading in Python. The idea is to create a pool of worker threads and then assign tasks to them as needed. This allows you to take advantage of multiple CPU cores and process tasks in parallel.

Using a lock to synchronize access to shared resources -

When working with multithreading in python, locks can be used to synchronize access to shared resources among multiple threads. A lock is an object that acts as a semaphore, allowing only one thread at a time to execute a critical section of code. The lock is released when the thread finishes executing the critical section.

Conclusion -

As you can see, the threading module provides a simple and efficient way to implement multithreading in Python. Whether you need to create a new thread, run a function across multiple input values, or synchronize access to shared resources, the threading module has you covered.

In conclusion, the threading module is a powerful tool for parallelizing code in Python. Whether you are a beginner or an experienced Python developer, the threading module is an essential tool to have in your toolbox. With multithreading, you can take advantage of multiple CPU cores and significantly improve the performance of your code.


# Multiprocessing in Python -

Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. In this repl, we'll take a closer look at the multiprocessing module and its various functions and how they can be used in Python.

To use multiprocessing we need to create a process object which calls a start() method. The start() method runs the process and then to stop the execution, we use the join() method. Here's how we can create a simple process.

Functions -

• The following are some of the most commonly used functions in the multiprocessing module:

• multiprocessing.Process(target, args): This function creates a new process that runs the target function with the specified arguments.

• multiprocessing.Pool(processes): This function creates a pool of worker processes that can be used to parallelize the execution of a function across multiple input values.

• multiprocessing.Queue(): This function creates a queue that can be used to communicate data between processes.

• multiprocessing.Lock(): This function creates a lock that can be used to synchronize access to shared resources between processes.

Creating a pool of worker processes -

Creating a pool of worker processes is a common approach to using multiprocessing in Python. The idea is to create a pool of worker processes and then assign tasks to them as needed. This allows you to take advantage of multiple CPU cores and process tasks in parallel.

Using a queue to communicate between processes -

When working with multiple processes, it is often necessary to pass data between them. One way to do this is by using a queue. A queue is a data structure that allows data to be inserted at one end and removed from the other end. In the context of multiprocessing, a queue can be used to pass data between processes.

Using a lock to synchronize access to shared resources -

When working with multiprocessing in python, locks can be used to synchronize access to shared resources among multiple processes. A lock is an object that acts as a semaphore, allowing only one process at a time to execute a critical section of code. The lock is released when the process finishes executing the critical section.

Conclusion -

As you can see, the multiprocessing module provides a simple and efficient way to run multiple processes in parallel. Whether you need to create a new process, run a function across multiple input values, communicate data between processes, or synchronize access to shared resources, the multiprocessing module has you covered.

In conclusion, the multiprocessing module is a powerful tool for parallelizing code in Python. Whether you are a beginner or an experienced Python developer, the multiprocessing module is an essential tool to have in your toolbox.



# Decorators Used-

1) @decorator => To make a decorator/To decorate a function
2) @property => To make a getter
3) @property_name.setter => To make a setter
4) @staticmethod => To make a static method
5) @classmethod => Passes the first argument in function as class not an instance



# Where to go from here -

To continue your learning journey, consider exploring the following resources:

Python books: There are many excellent books on Python that can help you deepen your knowledge and skills. Some popular options include "Python Crash Course" by Eric Matthes, "Automate the Boring Stuff with Python" by Al Sweigart, and "Fluent Python" by Luciano Ramalho. I would also like to recommend "Hands on Machine Learning book by Aurélien Géron"

YouTube Projects: There are many YouTube projects available which can be watched after you have some basic understanding of python

Python communities: There are many online communities where you can connect with other Python learners and experts, ask questions, and share your knowledge. Some popular options include the Python subreddit, the Python Discord server, and the Python community on Stack Overflow.

GitHub repositories: GitHub is a great resource for finding Python projects, libraries, and code snippets. Some useful repositories to check out include "awesome-python" (a curated list of Python resources), "scikit-learn" (a machine learning library), and "django" (a web development framework).

Link to some resources
Tkinter - You can learn Tkinter which is used to create GUIs from here :
Machine Learning - I loved this playlist from Google Developers
Django - For Django, try the tutorial from the official documentation. Trust me its really good
Overall, the key to mastering Python (or any programming language) is to keep practicing and experimenting. Set yourself challenges, work on personal projects, and stay curious. Good luck!
