def factorial(num):
    product = 1
    for i in range(num):
        product = product * i
    return product

print(factorial(10))
