import math

def newRound(input1="1", input2="2", way="None"):
    if way=="floor":
        print(math.floor(float(input1) + float(input2)))
    if way=="ceil":
        print(math.ceil(float(input1) + float(input2)))
    else:
        print(round(float(input1) + float(input2)))

# Get input from user
num1 = input("first number:")
num2 = input("second number:")

# Run function roundDown without variables
newRound()

# Run function roundDown with variables
newRound(num1, num2, "floor")
newRound(num1, num2, "ceil")
newRound(num1, num2)