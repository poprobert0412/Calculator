from art import paint

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def add(a, b):
    return a + b
def substract(a, b):
    return a - b



operation = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(paint)
    num1 = int(input("What is the first number?: "))
    for n in operation:
        print(n)
    symbols = input("Pick an operation symbol from the line above: ")
    num2 = int(input("What is the second number?: "))
    function = operation[symbols]
    answer = function(num1, num2)
    print(f"{num1} {symbols} {num2} = {answer}")

calculator()