number = int(input("Enter a number"))

try:
    print(20 / number)
    print("number printed")
except ZeroDivisionError:
    print("Number divided by zero error")
except TypeError:
    print("Give valid inputs!!!")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("something went wrong!")
finally:
    print("do some clean up here")