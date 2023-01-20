def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b
def mod(a,b): return a%b
def get_menu_choice():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. QUIT")
    a = eval(input("Enter the number of your choice: "))
    while a not in range(1,7):
        a = eval(input("Enter a number between given choices: "))
    return a

a, b = map(eval, input("Enter two values: ").split())
choice = 0
while choice != 6:
    choice = get_menu_choice()
    match choice:
        case 1:
            print(f"{a} + {b} = {add(a,b)}\n")
        case 2:
            print(f"{a} - {b} = {sub(a,b)}\n")
        case 3:
            print(f"{a} * {b} = {mul(a,b)}\n")
        case 4:
            print(f"{a}/{b} = {round((div(a,b)),2)}\n")
        case 5:
            print(f"{a}  mod {b} = {mod(a,b)}\n")
        case _:
            print("You chose to Quit")
