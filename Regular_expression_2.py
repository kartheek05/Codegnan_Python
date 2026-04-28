'''
7.?
--> This meta character will form a searching pettern as it will take any zero or one character for (?).
Synatx: re.findall(".?",variable_name)

import re
kk = "This meta character will from a searching pattren as it will take any one or more character for (+)."
any = re.findall("Th.?",kk) # it will search only 0 ot 1 occurence
ss = re.search("Th.?",kk)
#print(any)
print(ss)

8.{}
--->This meta character will formm a searching pattern as we can mention the size in the {}.
import re
any = "This meta character will from a searching pattren as it will take any one or more character for (+)."
kk = re.findall("se.{25}",any)
s = re.search(".{}",any)
print(s)
print(kk)

9. | 
This meta character will form a searching pattern as it consider right or left any string is present or not for (|).
import re
any = "This meta character will form"
an = re.findall("that|will",any)
print(an)
<---------------------------------------------------------------------------------------------------------------------------------------------------->
Special Sequence - A specaial sequence is a \ followed by one of the character in the list below, and has a 
A special sequence is a \ followed by one of the character are the beginning of the string.
Eg: "\AThe"
import re
txt = "The rain in spain"
#check if the string starts with "The"
x = re.findall("\AThe",txt)
print(x)
if x:
    print("yes,there is a match")
else:
    print("No match")

\b :Return a match where the specified character are the benginning or at the end od a word.
Eg: r"\bain"     
import re
txt = "The rain in spain"
x = re.findall(r"\bSpain",txt)
print(x)
if x:
    print("yes,there is at least one match")
else:
    print("no mtch")

3. \d - returns a match  where the string contains digits (number from0-9)
Eg: "\d" 

import re
txt = " The rain  in 56 Spain"
#Check if  the string contains any digits (number from 0-9):
x = re.findall("\d",txt)
print(x)
if x:
    print("yes, there is at least one match !")
else:
    print("no match")    
'''
'''
Time and Day:
%d -----> Day
%m -----> Month
%Y -----> Year
%H -----> Hours
%M -----> Minutes
%S -----> Seconds
%p -----> AM/PM
%A -----> Day Name
%B -----> Month Name
'''
# import datetime
# any = datetime.datetime.now()
# print(any)

# import datetime
# today = datetime.date.today()
# print(today.strftime("%d-%m-%Y"))
# print(today.strftime("%A"))
# print(today.strftime("%B"))

# import datetime
# today = datetime.datetime.today()
# print(today.strftime("%H-%M-%S"))