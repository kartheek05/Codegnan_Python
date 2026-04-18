'''
Self----> This keyword is instance variable and unique for each object.

Constructor----> The (__init__) function is called as constructor.
---->A constructor is a special method used to initiallize object data.
---->eg:__init__()

class student:
    def __init__(self, Name, Id, Age, Course, Days):
        self.Name = Name
        self.Id = Id
        self.Age = Age
        self.Course = Course
        self.Days = Days
    
    def display(self):
        print(self.Name,self.Id,self.Age,self.Course,self.Days)
stu_1 = student("Kartheek",33,22,"PFS","30Days")
stu_2 = student("Kumar",3,21,"JFS","30Days")
stu_1.display()
stu_2.display()
'''
''''
Acess Specifiers -----> These are Three types 
1.Public
2.Protected
3.Private

1.Public---->
Syntax: name 
we can use this any where in the Program.

2.Protected ----->
Synatax: _name
This is only for internal use.

3.Private ------>
Syntax: __name
This one is restricted.

class some:
    def __init__(self):
        self.public = "Public"
        self.protected = "Protected"
        self.private = "Private"

any = some()
print(any.public)
print(any._protected)
print(any.__private) 
'''
 
HDFC_KK_AC_det = {"Name" : "Kartheek","Pin" : "3303","Balance" : 1000,"History" : []};
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
                HDFC_KK_AC_det['History'].append(f"Withdraw amount {money_w}")
                print(f"Balance amount is: {HDFC_KK_AC_det['Balance']}")
                print(HDFC_KK_AC_det['History'])
            else:
                    print("INSUFFICIENT FUNDS")
        elif User_choice == 2:
            Deposite_M = int(input("Enter the Deposite Amount: "))
            if Deposite_M % 100 == 0 and Deposite_M >= 500:
                HDFC_KK_AC_det['Balance'] += Deposite_M
                HDFC_KK_AC_det['History'].append(f"Deposited money {Deposite_M}")
                print(HDFC_KK_AC_det['History'])
                print(f"You have deposited {Deposite_M} and The Balance is {HDFC_KK_AC_det['Balance']}")
            else:
                print(f"Please Enter the Valid Amount or Minimun Amount {Deposite_M}")
        elif User_choice == 3:
            attempts = 3
            while attempts > 0:
                check_pin = input("Enter the old PIN")
                if check_pin == HDFC_KK_AC_det['Pin']:
                    New_PIN = input("Enter the NEW PIN: ")
        elif len(New_PIN ) == 4:
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
            print(f"Your Transcation History{HDFC_KK_AC_det['History']}")
        else:
            print(f"Please enter the correct PIN {pin_1}")
            else:
                print("Enter Correct PIN")
    else:
        print("Please Enter the 4 Digit Pin")

# class Banking_System:
#     HDFC_KK_AC_DET = {"Name":"Kumar Kartheek","PIN":""}
