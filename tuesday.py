def factorial(num):
    product = 1
    for i in range(1,num):
        product = product * i
    return product
def reverse(str):
    return str[::-1]

fact = str(factorial(34234))

numOfZeros = 0
for digit in reverse(fact):
    if (digit == "0"):
        numOfZeros += 1
    else:
        break
print(numOfZeros)

