def greetGenerally() :
    print("Hello, How are you...")

def greet(name, age) :
    print(f"Hello, How are you {name}")
    print(f"I know your age is {age}")

def greetWithDefaults(name = "Mohamed", age = -1) :
    print(f"Hello {name}, how you doing")
    if(age >= 0):
        print(f"I know your age {age}")

greetGenerally()
greet("Haroon", 21)
greetWithDefaults(age = 21)
greetWithDefaults("haroon")
greetWithDefaults(name = "mohamed haroon", age = 21)
greetWithDefaults()
greetWithDefaults(name = "moharoon")


def isAdult(age) :
    return age >= 16

print(isAdult(21))

def genderIdentification(gender = "unknown") :
    if gender.upper() == "M" :
        return f"Your gender is Male"
    elif gender.upper() == "F" :
        return f"Your gender is Female"
    elif gender == "unknown" :
        return f"Your gender will be either Male or Female"
    else:
        return f"Your gender will be either Male or Female from else"

print(genderIdentification("m"))
print(genderIdentification("M"))
print(genderIdentification("f"))
print(genderIdentification("F"))
print(genderIdentification())
print(genderIdentification("YYY"))