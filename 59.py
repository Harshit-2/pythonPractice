def greet(fx):
    def mfx(*args, **kwargs):   # *args, **kwargs are used to pass any number of arguments to the function
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx  # mfx stands for modified function


@greet
def hello():
    print("Hello Japan")


@greet
def add(a, b):
    print(a+b)


# greet(hello)()    # Decorate the function at line 9 or run it like this its the same thing but its complicated to do it this way better to use the @greet
hello()
# greet(add)(1, 2)
add(1, 2)


#   Logging

# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(
#             f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated


# @log_function_call
# def my_function(a, b):
#     return a + b
