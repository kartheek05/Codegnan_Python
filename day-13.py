#Patterns
'''
num = int(input("Enter the Limit: "))
for j in range(num+1): #This is used for the up to down 
    for i in range(j): #T
        print(j,end = "")#
    print()# To get new line
*
**
***
****
*****

<------------------------------------------------------------------------------------------------------------------>
num = int(input("Enter the Limit: "))
for j in range(num+1):
    for i in range(j):
        print(i,end = "")#
    print()# To get new line
1
22
333
4444
55555
<------------------------------------------------------------------------------------------------------------------>
num = int(input("Enter the Limit: "))
for j in range(num):
    for i in range(num):
        print("*",end = "")#
    print()# To get new line
***
***
***
***
<------------------------------------------------------------------------------------------------------------------>
num = int(input("Enter the Limit: "))
for j in range(num):
    for i in range(num-j):
        print("*",end = "")#
    print()# To get new line
******
*****
****
***
**
*
<------------------------------------------------------------------------------------------------------------------>
num = int(input("Enter the Limit: "))
for i in range(num):
    print(" " * (num-i),end = "")
    for j in range(i+1):
        print("*" ,end = " ")
    print()
* 
    * * 
   * * * 
  * * * * 
 * * * * * 
<------------------------------------------------------------------------------------------------------------------>
num = int(input("Enter the Limit: "))
for i in range(num):
    print(" " * (num-i),end = "")
    for j in range(i+1):
        print("*" ,end = " ")
    print()

m = int(input("Enter the Input: "))
for i in range(m):
    print(" " * (m-i), end = "")
    for j in range(i+1):
        print("*",end = " ")
    print()
'''
#Pin Checker
HDFC_KK_AC_det = {"Name" : "Kartheek",
                                      "Pin" : "3303",
                                      "Balance" : 10000};
print("Welcome to HDFC Bank ATM")
print("Please insert your ATM Card")
HDFC_User_Pin = input("Please Enter your 4 digit ATM Pin: ")
if len(HDFC_User_Pin) == 4:
    if HDFC_User_Pin in HDFC_KK_AC_det['Pin']:
        print("Correct Pin")
        User_choice = int(input("Enter  \n1.Withdraw: "))
        if User_choice == 1:
            money_w = int(input("Enter The Amount: "))
            if money_w <= HDFC_KK_AC_det['Balance']:
                HDFC_KK_AC_det['Balance'] -= money_w
                print(f"Balance amount is: {HDFC_KK_AC_det['Balance']}")
            else:
                print("INSUFFICIENT FUNDS")
    else:
        print("Enter Correct PIN")
else:
    print("Please Enter the 4 Digit Pin")



















