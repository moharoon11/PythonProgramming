# Dynamic type allocation
name = "Mohamed Haroon"
age = 21
cgpa = 73.81
isEarning = False
isGoodAtProgramming = True
numbers = [1,2,3,4,5,6]

def sayHello() :
    return "Hello " + name

print(sayHello())

# Manual allocation
secondName: str = "Umar"
monthBorn: int = 4
timeBorn: float = 11.49
isCriedAfterBorn: bool = True
isNotProgrammingRightNow: bool = False
oddNumbers:list = [1,3,5,7,9,11]


def sayHi() -> str :
    return "hi " + secondName

print(type(name))
print(type(secondName))

print(type(cgpa))
print(type(isCriedAfterBorn))

print(type(age))
print(type(monthBorn))

print(sayHi())


