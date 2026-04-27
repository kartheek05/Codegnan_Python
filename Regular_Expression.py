'''
Regular Expressions(RegEx):
---->This is Regular Expression or RegEx is a sequence of characters that forms a searching patterns.
---->To use this we have to import re ,which will nlock the package.

Functions:
1.Findall: By using this function, it will find all sequence in the string.
Syntax--> re.findall("metachar",variable_name)

2.Search: By using this Function, it only find first sequence in the string
Syntax---> re.search("metachar",variable_name)

Example:
import re 
any = "Kartheek"
kk = re.findall("K",any)
print(kk)
ss = re.search("k",any)
print(ss)

MetaCharacters:
Metacharacters are used to form searching pattern. They are
1.[] --> In this meta character we can search for [a-z], [A-Z], [0-9]

import re
any = "By using this Function, it only find first sequence in the string"
so = re.findall("[aeh]",any)# This will all the elements in list
kk = re.findall("[a-z]",any)
print(kk)
print(so)

2.dot(.)--> This ,eta character will search form form a searching pattern and i will take any single character for (.). 

import re
we = "hello"
the = re.findall("h...o",we)
kk = re.search("h...o",we)
print(the)
print(kk)

3.^---> This is used to find the string is starting with the sequence.

import re
how = "This is Regular Expression or RegEx is a sequence of characters that forms a searching patterns."
who = re.findall("^This is", how)
then = re.search("^This",how)
print(who)
print(then)

4.$----> This is used to find the string is ending with the sequence or not.
Synatx: re.findall("$",variable_name) 

import re
out = "This is used to find the string is ending with the sequence or not."
one = re.findall("sequence $",out)
two = re.search("This$", out)
print(one)
print(two)

5.*
--> This meta character will form a searching pattern as it will take any zero or more character for (*)

import re
teja = "This meta character will form a searching pattern as it will take any zero or more character for (*)"
gk = re.findall("c.*i",teja)
ll = re.search("T.*",teja)
print(gk)
print(ll)

6.+
--->This meta character will from a searching pattren as it will take any one or more character for (+).
Syntax --> re.search(".+",variable_name)

import re
kk = "This meta character will from a searching pattren as it will take any one or more character for (+)."
lk = re.findall("mo.+e",kk)
kol = re.search("T.+",kk)
print(kol)
print(lk)
'''
