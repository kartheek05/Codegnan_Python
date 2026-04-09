'''
Lambda function()-------->
-->This is a also called as a Anonymous fuction.
-->A lambda function can take n number of arguments but have only one expression.
Syntax-->
lambda(keyword)arguments : expression
Examples:

#Example_1
any = lambda so , do : so + do
print(any(6,10))
print(any(int(input("Enter")),int(input("enter"))))

#Example_2
more = lambda kar , kum , theek : (kar + theek)*kum
print(more(int(input("enter")),int(input("enter")),int(input("enter"))))

List Comprehension:
--->This offers the shorter syntax when you want to create a new list form the exisiting list
Syntax ----> variable_name = [enpression loop and condition]
'''
old_list = [1,2,3,4,5,6]
new_list = [j for j in old_list if j % 2 == 0]
print(new_list)
