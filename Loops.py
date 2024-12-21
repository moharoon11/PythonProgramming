numbers = [1,2,3,4,5,6,7]

for num in numbers:
    print(num)

namesSet = {"mohamed haroon", "Mohamed Haroon", "mohamed haroon", "Haroon", "Haroon"}

for name in namesSet:
    print(name)

person = {
    "name" : "Mohamed Haroon",
    "age" : 21.7,
    "frontend_skill" : {"html", "css", "js", "react"},
    "backend_skill" : {"Java", "Python", "J2EE", "Hibernate", "Spring Boot", "etc"},
    "favourite_sports" : ["Football", "Settle Cork"],
}

for key in person:
    print(f"key = {key} -> value = {person.get(key)}")

for key in person:
    print(f"key = {key} -> value = {person[key]}")


for key in person.keys():
    print(f"Key = {key}")

for value in person.values():
    print(f"value = {value}")

for key, value in person.items():
    print(f"key = {key} -> value = {value}")


# While loop

number1 = 1
num = 1

while num <= 10:
    print(num)
    num+=1

while number1 <= 10:
    print(number1)
    number1+=1
else:
    print(f"value of number in after reaching else is {number1}")



pointer = 0
while pointer <= 10:
    if pointer == 5:
        print(f"The value of pointer is {pointer}")
    pointer+=1

pointer1 = 0
while pointer1 <= 10:
    if pointer1 == 5:
        print(f"The value of pointer is {pointer1}")
        break
    pointer1+=1



for oddNum in [1,2,3,4,5,6,7,8,9,10, 11, 12, 13,14,15, 16, 17, 18, 19, 20]:
    if oddNum % 2 == 0: continue
    print(oddNum)


randomNumber = 0

while randomNumber <= 10:
    if randomNumber < 5 :
        randomNumber += 1
        continue
    print(randomNumber)
    randomNumber+=1









