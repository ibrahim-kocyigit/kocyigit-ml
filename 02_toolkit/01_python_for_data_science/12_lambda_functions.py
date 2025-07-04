# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What is a Lambda Function?
# 2. Lambda Syntax vs. Regular Functions
# 3. The Primary Use Case: With High-Order Functions
# 4. Lambdas & Readability


# =======================================
# 1. WHAT IS A LAMBDA FUNCTION?
# =======================================
# - A small, single-expression, anonymous function.
# - "Anonymous" because it's not defined with the `def` keyword and has no name.
# - Syntax: `lambda arguments: expression`
# - The `expression` is evaluated and its result is automatically returned.
# - Can have any number of arguments but only one expression.
# - Best for short, simple, one-time use functions.


# =======================================
# 2. LAMBDA SYNTAX VS. REGULAR FUNCTIONS
# =======================================
# - A lambda provides a shorthand for writing simple functions.

# Regular function using `def`
def square(x):
    return x * x


# Equivalent lambda function
square_lambda = lambda x: x * x

print(f"Result from regular function: {square(5)}")
print(f"Result from lambda function: {square_lambda(5)}")

# Another example with multiple arguments
add_lambda = lambda x, y: x + y
print(f"Result from multi-argument lambda: {add_lambda(10, 20)}")
print("-" * 30)

# - The reason your IDE is probably complaining for the functions above is that
#   lambda functions are not supposed to be assigned to variables and used afterwards. Instead:


# =======================================
# 3. THE PRIMARY USE CASE: WITH HIGHER-ORDER FUNCTIONS
# =======================================
# - Lambda functions are most powerful when used as an argument to another function
#   that takes a function as input (a "higher-order function").
# - Common examples: `sorted()`, `map()`, `filter()`.


# --- Use with `sorted()` ---
# Sort a list of tuples based on the second element (the age)
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]

# The `key` argument of `sorted()` needs a function that takes one item and returns what to sort by.
# A lambda is perfect here.
sorted_students = sorted(students, key=lambda student: student[1])
print(f"Students sorted by age: {sorted_students}")

# Sort a list of dictionaries by a value
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
]
sorted_products = sorted(products, key=lambda product: product["price"])
print(f"Products sorted by price: {sorted_products}")
print("-" * 30)

# --- Lambdas with `.map()` and `filter()`
# The most common use case of lambda functions is with `.map()` and `.filter()`
# We'll be covering these use cases in 13_higher_order_functions.py


# =======================================
# 4. LAMBDAS & READABILITY
# =======================================
# - While lambdas are concise, they can harm readability if overused or made too complex.
# - A rule of thumb: If a lambda is longer than one line or hard to understand at a glance,
#   it's better to use a regular `def` function.


# --- Example of a less readable lambda ---
# This is valid, but confusing. A `def` function would be clearer.
complex_lambda = (
    lambda x: "High" if x > 100 else ("Medium" if 50 <= x <= 100 else "Low")
)


# --- Clearer `def` function ---
def get_level(x):
    if x > 100:
        return "High"
    elif 50 <= x <= 100:
        return "Medium"
    else:
        return "Low"


print(f"Complex lambda result: {complex_lambda(75)}")
print(f"Regular function result: {get_level(75)}")


# --- End of File ---
