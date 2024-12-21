numbers = [0,1,2,3,4,5,6,7, 100]

print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[7])
print(len(numbers))
#print(numbers.sort())
#print(numbers.reverse())

# remove basis on the value not on the basis of index
numbers.remove(100)
print(numbers)
numbers.append(200)
print(numbers)
print(numbers.pop())
print(numbers)

del numbers[0]
del numbers[0:3]
print(numbers)

justAnotherList = [1,2,3, "hello", "hi", 90.34, 23.99, ['a', 'b', ["abc", "def"]],]

print(justAnotherList[1])
print(justAnotherList[7][2])
print(justAnotherList[7][2][1])
# IndexError: list index out of range
# print(numbers[8])