while (True):
    answer: str = input("How old are you?")


answer: str = input("Hove old are you?")

# Check if input between 0 and 99
number = int(answer)
# 1. Check if vaild number
try:
    number = int(answer)
except ValueError as err:
    print(err)
    pirnt("Give valid number")
    continue

state: str = ""

if 0 < number and number <= 99:
    # OK
    if number <= 25:
        state = "young"
    elif number < 50:
        state = "default"
    elif number < 75:
        state = "elredly"
    elif number <= 99:
        state = "ghost"

match state:
    case "young":
        print("Lucky")
    case "adult":
        print("♥")
    case "elder":
        print("Legend")
    case "ghost":
        print("Fart")
    case _:
        pass
