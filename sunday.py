def sumMultiplesQ1(number):
    sum = 0
    for i in range(number):
        if(i % 3 == 0 and  i % 5 == 0):
            sum += i
        elif (i % 3 == 0 or i % 5 == 0):
            sum += i        
    if(number % 3 == 0 or number % 5 == 0):
        sum += number
    return sum

print(sumMultiplesQ1(3452342))


