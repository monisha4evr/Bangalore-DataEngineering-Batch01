function 
    # Resuable block of Code 
    # to perform some specific Task 

Syntax: 

# declaration/definition
def function_name():
    # statement  

# function calling 
function_name()

def greet():
    print("Welcome to Function in Python ")

greet()
greet()
greet()
greet()
greet()

types: 
1. built -in  function -  input(),print()
2. user defined function 
3. lambda 
4. recursion 


user-defined function 

    # created by programmers based on their requirement 

Argument: Actual value 
parameter: Alias Name 


def add(a,b):
    print(a+b)

add(10,20)

return =>  pass the result and come out from the function



def add(a,b):
    print("i am inside the Function")
    return a+b 
    print("Welcome to the Function")

print(add(20,10))


def add(a,b):
    print("i am inside the Function")
    return a+b 
    print("Welcome to the Function")

x=10
y=20
print(add(x,y)) 



 4 types
    1. witout  Argument - without Return
    2. without Arguments - with return 
    3. with Argument - without Return 
    4. with Arguments - with Return 



 1. witout  Argument - without Return 


def greet():
   print("this is Example for Function")

greet()

 2. without Arguments - with return


x=10
y=20 
def add():
   return x+y

res=add()
print(res)


def add():
    x=10
    y=20 
    return x+y

res=add()
print(res)

def add():    
    return 50+30

print(add())


3. with Argument - without Return  

def mul(a,b):
   print(a*b)

print(mul(12,5))



 4. with Arguments - with Return  

def calculation (operator,a,b):
   if operator == '+':
      return a+b
   elif operator == '-':
        return a-b 
   elif operator == '*':
        return a*b 
   else :
      return "No Operation"

print(calculation('+',10,20))
print(calculation('*',10,20))
print(c)
c=100
def calculation (operator,a,b):
   c=50
   if operator == '+':
        c+= a+b
   elif operator == '-':
        c= a-b 
   elif operator == '*':
        c= a*b 
   else :
        c= "No Operation"
   return c

#print(c)
print(calculation('+',10,20))
print(calculation('*',10,20))



Argument Types: 
---------------- 

1. positional argument 
2. keyword argument 
3. default argument 
4. arbitary argument 

1. Positional Argument
    # arguments are passed based on their Position(order)

def add(a,b):
    print(a)
    print(b)
    print(a+b)

add(89,20)

2. Keyword Argument 

def add(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    print(a+b+c+d)

add(b=89,d=20,c=30,a=40)
add(b=89,d=20,o=30,a=40) # TypeError: add() got an unexpected keyword argument 'o'


def add(a,b):
    print(a)
    print(b)

add(10) # TypeError: add() missing 1 required positional argument: 'b'
add(10,20,30) # TypeError: add() takes 2 positional arguments but 3 were given

# parameter and Argument count must be same

3. default argument 


def add(a,b,c=0,d=None):
    print(a)
    print(b)
    print(c)
    print(d)

add(10,20)
add(10,20,50)
add(10,20,50,60)

4. arbitary argument  (packing the variable)
    1. *  - store rest of the values to the single variable
    2. ** - 

def sample(x,z,*y):
    print(x)
    print(z)
    print(y)

sample(1,2,3,4,5,6)

def sample(x,z,**y):
    print(x)
    print(z)
    print(y)

sample(x=1,z=2,a=3,b=4,c=5,y=6)

def test(a,b,c):
    print(a)
    print(b)
    print(c)

test(30,c=20,b=80)
test(c=10,20,30) # SyntaxError: positional argument follows keyword argument


# positional only
def test(a,b,c,/):
    print(a)
    print(b)
    print(c)

test(30,20,80)
test(30,c=20,b=80) # TypeError: test() got some positional-only arguments passed as keyword arguments: 'b, c'


def test(a,/,b,c):
    print(a)
    print(b)
    print(c)

test(30,c=20,b=80)


# Keyword only
def test(a,*,b,c):
    print(a)
    print(b)
    print(c)

test(30,c=20,b=80)
test(30,20,80) # TypeError: test() takes 1 positional argument but 3 were given