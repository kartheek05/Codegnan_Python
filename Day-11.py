'''
#Table Generator
N = int(input("Enter the Table you want: "))
s = int(input("Enter the range: "))
for i in range(1,s+1):
    print(f"{N} X {i} = {N*i} ")
<------------------------------------------------------------------------------------------------------------------------------------->
#Methods--------------> count(),join(),strip(),replace(),split(),capitalize(),casefold(),isalnum(),isalpha(),isdigit(),isdecimal(),islower(),isupper()
<------------------------------------------------------------------------------------------------------------------------------------->
#Total small and capital letters in input
n = input("Enter the Sentence: ")
count_1 = 0
count_2 = 0
count_3 = 0
C_list = []
S_list = []
for i in n:
    if i.islower():
        count_1 += 1
        C_list.append(i)
    elif i in (" "):
        count_3 += 1
    else:
        count_2 += 1
        S_list.append(i)
print(f"The Lower Case are: {count_1}\nThe Upper Case are: {count_2}\nThe Spaces are: {count_3}")
print(f"The Small Letters are {S_list}\nCapital Letters are {C_list}")
<------------------------------------------------------------------------------------------------------------------------------------->
#Pin Checker
HDFC_KK_AC_det = {"Name" : "Kartheek",
                                      "Pin" : "2303"}
print("Welcome to HDFC Bank ATM")
print("Please insert your ATM Card")
HDFC_User_Pin = input("Please Enter your 4 digit ATM Pin: ")
if len(HDFC_User_Pin) == 4:
    if HDFC_User_Pin in HDFC_KK_AC_det['Pin']:
        print("Correct Pin")
    else:
        print("Enter Correct PIN")
else:
    print("Please Enter the 4 Digit Pin")
<------------------------------------------------------------------------------------------------------------------------------------->

#Perfect Number
num = int(input("Entre the Number: "))
count = 0
for i in range(1,num):
    if num % i == 0:
        count += i
if count == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")
<------------------------------------------------------------------------------------------------------------------------------------->
'''
