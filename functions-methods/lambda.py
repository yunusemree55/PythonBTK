
def square(number) : return number**2


numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(map(square,numbers))
print(result)


check_even = lambda number : number % 2 == 0

result = list(filter(check_even,numbers))
print(result)
