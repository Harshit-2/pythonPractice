numbers = [1, 2, 3, 4, 5]   # List of numbers
doubled = map(lambda x: x * 2, numbers) # Double each number using the map function
print(list(doubled))    # Print the doubled numbers


numbers = [1, 2, 3, 4, 5]   # List of numbers
evens = filter(lambda x: x % 2 == 0, numbers)   # Get only the even numbers using the filter function
print(list(evens))  # Print the even numbers


from functools import reduce

numbers = [1, 2, 3, 4, 5]   # List of numbers

# numbers = [3, 3, 4, 5]    # This is how reduce works
# numbers = [6, 4, 5]
# numbers = [10, 5]
# numbers = [15]

sum = reduce(lambda x, y: x + y, numbers)   # Calculate the sum of the numbers using the reduce function

print(sum)  # Print the sum
