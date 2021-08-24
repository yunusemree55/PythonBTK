
numbers = [1,10,5,16,4,9,10]
letters = ["a","b","c","d","e"]

val = max(numbers)
val = min(numbers)

val = max(letters)
val = min(letters)

val = numbers[2:4]
val = numbers[::-1]
print(val)

numbers.append(50)
numbers.insert(0,20)
numbers.pop()
numbers.pop(0)
numbers.remove(16)
numbers.sort()
letters.sort()
letters.reverse()
print(numbers)
print(letters)

value = numbers.count(10)
print(value)
