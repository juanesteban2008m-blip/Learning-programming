import os
os.system('clear')
#inputs
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: ") )

#main menu 
def main_menu():
    print("#### MAIN MENU ####")
    print("[1]. Addition")
    print("[2]. Substraction")
    print("[3]. Multiplication")
    print("[4]. Division")
    print("[5]. Average")
    print("[6]. All operations")
main_menu()
opt = int(input("Enter any option: "))

if (opt == 1): 
    add = n1 +n2 
    print(f"addition is: (add)")

elif (opt == 2) 
    subs = n1 - n2 
    print(f"substraction is: (subs)")

    elif (opt == 3) 
    mult= n1 * n2 
    print(f"Multiplication is: (mult)")

elif (opt == 4) 
    div = n1 / n2 
    print(f"Divisionis: (div)")

    elif (opt == 5) 
    avg= n1 * n2 
    print(f"Average is: (avg)")

    elif (opt == 6) 
    add= n1 + n2 
    subs = n1 - n2 
    mult= n1 * n2 
    div = n1 / n2 
    avg= n1 * n2 
    print(f"addition  is: (add)")