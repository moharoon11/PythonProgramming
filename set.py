numbersSet = {1, 2, 3, 3, 4, 4, 5, 5, 6}
print(numbersSet)
lettersSet = {'a', 'b', 'b', 'c', 'd', 'd', 'e'}
print(lettersSet)

justAnotherSet = {1, 'a', 'a', "haroon", "haroon", 2.34, 77.999, False, True}
print(justAnotherSet)


lettersA = {'A', 'B', 'C', 'D', 'E', 'F'}
lettersB = {'E', 'F', 'G'}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersB - lettersA 

print(f"Union = {union}")
print(f"Intersection = {intersection}")
print(f"Difference = {difference}")