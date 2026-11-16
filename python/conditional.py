Conditional statement: 

execute block of code based on a condition 


age=25 
if age==20 : 
    print("your age is 20")


types: 

if 
if-else 
if elif else 
nested if 
ternary operator 

if statement: 
    - it execute only when the given condition is true

Syntax: 

if condition : 
    statement 


a=1

print("Simple if Condition")
if a>5 :
    print("A is Greater than 5")
    print("welcome to conditional statement")

print("Program Ended")

num=1
if num>10:
    print("condition is True")
    print("i am inside if block")
    num+=10 # num=num+10
    print(num)

print("Outside")


if - else 

=> excute  if block, if the condition is true,otherwise it execute else block  

Syntax: 

if condition :
    # True block 
else : 
    # False block  

num=11

if num%2==0 :
    print(num," is Even")
else : 
    print(num, " is Odd ")


a=1

if a>0:
    print(a, " is Positive Number")
else:
    print(a, " is Negative Number") 

if False:
    print("Welcome")
else:
    print("go")

if 1:
    print("Welcome")
else:
    print("go")



if elif else :
    => check multiple condition

Syntax: 

if condition:
    statement 
elif condition :
    statement 
elif condition:
    statement 
else:
    statement 

num = -10
if num > 0: 
    print("Positive")
elif num < 0:
    print("Negative")
else : 
    print("Zero")

marks=75

if marks >=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else:
    print("Fail")


# this executes the first matching condition
marks=100

if marks >=50:
    print("Grade C")
elif marks>=70:
    print("Grade B")
elif marks >=90:
    print("Grade A")
else:
    print("Fail")

nested if Statement  
=>  if statement placed inside another if statement 


if condition1:
    if condition2:
        statement1
    else:
        statement2 
else:
    statement 


a=20
b=10
c=30

if a>b :
    if a>c:
        print(" A is greater")
    else:
        print(" C is Greater ")
else:
    print("B is Greater")


a=45
if a%2==0 :
    print("A is Even")
else:
    print("A is ODD")


# ternary Operator
Syntax: value_if_true if condition else value_if_flase

a=46 
print( " Even Number" if a %2==0  else " Odd Number" )


