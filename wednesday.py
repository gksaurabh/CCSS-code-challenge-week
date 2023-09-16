from math import sqrt
def numOfDivisors(num):
    numberOfDivisors = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            numberOfDivisors += 1
    return numberOfDivisors



# i = 17000000
# while (numOfDivisors(i) != 419):
#     print("i: ", i, " Number of Divisors: ", numOfDivisors(i))
# #     i += 1
# print(i)
def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # If i is a divisor, check if both divisors are the same (perfect square)
            if n // i == i:
                divisors += 1
            else:
                divisors += 2
    return divisors

def find_number_with_divisors(d):
    n = 1
    while True:
        if count_divisors(n) == d:
            return n
        n += 1

d = 420

result = find_number_with_divisors(d)
print(result)