def factorial(number):
    if number == 0 and number == 1:
        print("Sonuç: 1")
    if number < 0:
        raise ValueError("Number must be positive")
    
    def inner_factorial(number):
        if(number == 1):
            return 1
        return number * inner_factorial(number-1)
    
    return inner_factorial(number)


result = factorial(6)

print(result)

