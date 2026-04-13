'''
Generators ---->
----->This is a special Type of function that return an ITERATOR which one at a time.

def my_generator():
    yield 1 #it is like a return function 
    yield 2 #here these will come one after one 
    yield 3
an = my_generator()
print(next(an))
print(next(an))
print(next(an))

yield-------->
------->It will take a pause and again resume, this is not a normal keyword cannot be used in the nomal functions.
------->This is used to produce a value and pause execution.

Next------>
------>This is used to get value from a generator
------>When the value is finished, it will stop the iterator 
def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(5):
    print(val)
'''

while True:  
        HDFC_KK_AC_det = {"Name" : "Kartheek",
                                              "Pin" : "3303",
                                              "Balance" : 10000,
                                              "History" : []};
        print("Welcome to HDFC Bank ATM")
        print("Please insert your ATM Card")
        HDFC_User_Pin = input("Please Enter your 4 digit ATM Pin: ")
        if len(HDFC_User_Pin) == 4:
            if HDFC_User_Pin in HDFC_KK_AC_det['Pin']:
                print("Correct Pin")
                User_choice = int(input("Enter  \n1.Withdraw: \n2.Deposite \n3.Pin Change \n4.Transaction History"))
                if User_choice == 1:
                    money_w = int(input("Enter The Amount: "))
                    if money_w <= HDFC_KK_AC_det['Balance']:
                        HDFC_KK_AC_det['Balance'] -= money_w
                        HDFC_KK_AC_det['History'] . append(f"Withdraw amount : {money_w}")
                        print(f"Balance amount is: {HDFC_KK_AC_det['Balance']}")
                    else:
                        print("INSUFFICIENT FUNDS")
                elif User_choice == 2:
                    Deposite_M = int(input("Enter the Deposite Amount: "))
                    if Deposite_M % 100 == 0 and Deposite_M >= 500:
                        HDFC_KK_AC_det['Balance'] += Deposite_M
                        HDFC_KK_AC_det['History'] . append(f"Deposited amount : {Deposite_M}")
                        print(f"You have deposited {Deposite_M} and The Balance is {HDFC_KK_AC_det['Balance']}")
                    else:
                        print(f"Please Enter the Valid Amount or Minimun Amount {Deposite_M}")
                elif User_choice == 3:
                    attempts = 3
                    while attempts > 0:
                        check_pin = input("Enter the old PIN")
                        if check_pin == HDFC_KK_AC_det['Pin']:
                            New_PIN = input("Enter the NEW PIN: ")
                            if len(New_PIN ) == 4:
                                if HDFC_KK_AC_det['Pin'] != New_PIN:
                                    HDFC_KK_AC_det['Pin'] = New_PIN
                                    print(f"PIN changed Done {HDFC_KK_AC_det['Pin']}")
                                else:
                                    print("The NEW PIN shouldn't be the OLD PIN")
                            else:
                                    print(f"Please Entre 4 Digit PIN {New_PIN}")
                        else:
                            attempts -= 1
                            print(f"Please Enter the Correct OLD PIN \n you Have entered the worng PIN{check_pin} and \nThe NO.Of Attempts {attempts}")
                    if attempts == 0:
                        print("Please contact the Customers Care you have Reached the Limit")
                elif User_choice == 4:
                    pin_1 = input(f"Please Enter the 4 digit PIN: ")
                    if pin_1 == HDFC_KK_AC_det['Pin']:
                        print(f"Your Transcation History \n {HDFC_KK_AC_det['History']}")
                    else:
                        print(f"Please enter the correct PIN {pin_1}")
            else:
                print("Enter Correct PIN")
        else:
            print("Please Enter the 4 Digit Pin")

