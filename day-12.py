'''
Break---> This is used to exit form the loop, when we found the required vaue...
<------------------------------------------------------------------------------------------------------------>
for j in range(1,10):
    print(j)
    if j == 5:
        break
<------------------------------------------------------------------------------------------------------------>
lis_ = [1,2,3,4,56,]
for n in lis_:
    if n == 1:
        print(n)
    break #This control statement will work for only loops.
<------------------------------------------------------------------------------------------------------------>
lis_ = [1,2,3,4,56,]
for n in lis_:
    print(n)
    if n == 1:
        break #This control statement will work for only loops.
<------------------------------------------------------------------------------------------------------------>
lis_ = [1,2,3,4,56,]
for n in lis_:
    print(n)
    if n == 1:
        continue #this is used to skip that particular loop
<------------------------------------------------------------------------------------------------------------>
for j in range(1,10):
    if j == 5:
        continue
    print(j)
<------------------------------------------------------------------------------------------------------------>
Pass ------> This is called as space holder.
                    incase any statement like(if,for,else, elif....) This should be complete,
                    if not we get syntax error to avoid this we are using pass.
for j in range(1,100):
    pass
<------------------------------------------------------------------------------------------------------------>
Else -- for : This will fall back to else block, when all loops are completed

for m in range(1,10):
    print(m)
else:
    print("This Prints")

for m in range(1,10):
    if m == 12:
        print(m)
        break
else:
    print("This Prints")

<------------------------------------------------------------------------------------------------------------>
While() ----------- This is the combination of both if and for statement, if we did not end the loop in a proper way it will run
                            upto the memory space becomes Full.

num = 1
while num < 5:
    print(num)
    num += 1
<------------------------------------------------------------------------------------------------------------>

'''
user_in = int(input("Entre the Limit: "))
num_1 = 0
num_2 = 1
print(num_1, num_2, end=" ")
for v in range(user_in + 1):
    num_3 = num_2 + num_1
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")


