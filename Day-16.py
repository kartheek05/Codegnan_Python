'''
-----------------------------------Recurive function--------------------
Recursion is a programming technique where a function calls itself either directly or indirctly to solve a problem by breaking it into
smaller, simpler subproblem.
Recursion is especially useful for problem thta can be calcuations, tree traversals or divide-and-conqure algorithms.
Example:

def fibbonaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibbonaci(num-1) + fibbonaci(num-2)
print(fibbonaci(num = 7))
<---------------------------------------------------------------------------------------------------------------------------------------------------->

HDFC_KK_AC_det = {"Name" : "Kartheek",
                                      "Pin" : "3303"}
print("Welcome to HDFC Bank ATM")
print("Please insert your ATM Card")
def validate_pin():
    while remaining_attempts > 0:
        user_pin = input("Enter 4 digit Pin: ")
        if len(user_pin) == 4 and user_pin == HDFC_KK_AC_det["PIN"]:
            print("Welcome to the ATM")
            return True
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"Invaild Pin. Attempts left: {remaining_attempts}")
            else:
                print("Card blocked. Please contact customer care")
                return False
validate_pin()
<---------------------------------------------------------------------------------------------------------------------------------------------------->
any = input("Enter the Sentence: ").lower()
print(any)
def vo_co(any,count_1,count_2,count_3):
    for i in any:
        if i in "aeiou":
            count_1 += 1
        elif i == " ":
            count_2 += 1
        else:
            count_3 += 1
    print(f"The Total Consonants are {count_3} \n The Total Vowels are {count_1} \n The total Spaces are {count_2}")
vo_co(any,count_1 = 0,count_2 = 0,count_3 = 0)
<---------------------------------------------------------------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------------------------------------------------------------->
 '''           
HDFC_KK_AC_det = {"Name" : "Kartheek",
                                      "Pin" : "3303",
                                      "Balance" : 10000};
print("Welcome to HDFC Bank ATM")
print("Please insert your ATM Card")
HDFC_User_Pin = input("Please Enter your 4 digit ATM Pin: ")
if len(HDFC_User_Pin) == 4:
    if HDFC_User_Pin in HDFC_KK_AC_det['Pin']:
        print("Correct Pin")
        User_choice = int(input("Enter  \n1.Withdraw: \n2.Deposite"))
        if User_choice == 1:
            money_w = int(input("Enter The Amount: "))
            if money_w <= HDFC_KK_AC_det['Balance']:
                HDFC_KK_AC_det['Balance'] -= money_w
                print(f"Balance amount is: {HDFC_KK_AC_det['Balance']}")
            else:
                print("INSUFFICIENT FUNDS")
        elif User_choice == 2:
            Deposite_M = int(input("Enter the Deposite Amount: "))
            if Deposite_M % 100 == 0 and Deposite_M >= 500:
                HDFC_KK_AC_det['Balance'] += Deposite_M
                print(f"You have deposited {Deposite_M} and The Balance is {HDFC_KK_AC_det['Balance']}")
            else:
                print(f"Please Enter the Valid Amount or Minimun Amount {Deposite_M}")
    else:
        print("Enter Correct PIN")
else:
    print("Please Enter the 4 Digit Pin")
        
