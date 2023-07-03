import random
password=[]
pass_str=""
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=["@", "#", "$", "%", "&", "*", "(", ")", "!"]
print("\n\t\t\t\tWelcome to Password Generator!\n")
FN = input("Enter your First Name: ")
char = input("What kind of password do you want to create? (Easy/Hard): ")
if char=="Easy" or char=="easy" or char=="EASY":
    for i in FN:
        password.append(i)
    no_num=int(input("Enter no. of Numbers in the password: "))
    no_sym=int(input("Enter no. of Symbols in the password: "))
    for i in range(1,no_num+1):
        password += random.choice(numbers)
    for i in range(1,no_sym+1):
        password += random.choice(symbols)
    for i in password:
        pass_str += i
    print("Your Password is- ",pass_str)
    print("\n\t\t\t\tThank You!, for using our system.\n")

elif char=="Hard" or char=="hard" or char=="HARD":
    letters=[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    no_let=int(input("Enter no. of Letters in the password: "))
    no_num=int(input("Enter no. of Numbers in the password: "))
    no_sym=int(input("Enter no. of Symbols in the password: "))
    for i in range(1,no_let+1):
        password += random.choice(letters)
    for i in range(1,no_num+1):
        password += random.choice(numbers)
    for i in range(1,no_sym+1):
        password += random.choice(symbols)
    random.shuffle(password)
    for i in password:
        pass_str += i
    print("Your Password is- ",pass_str)
    print("\n\t\t\t\tThank You!, for using our system.\n")

else:
    print("\n\t\t\t\tAlert!, Please choose between 'Easy' or 'Hard'\n")
