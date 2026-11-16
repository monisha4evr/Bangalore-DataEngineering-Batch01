= special symbols 
=> to perform operation on values and variable

a=10
b=20
c=a+b

+ => operator 
a,b => operand 

a+b => expression 


Types:
1. Arithmetic operator 
2. assignment operator 
3. comparision operator 
4. logical operator 
5. bitwise operator 
6. membership operator 
7. identity operator


Arithmetic operator 
= > to perform mathematical operation 

a=10
b=3 

print("addition",a+b)
print("Subtraction",a-b) # 7
print("multiplication",a*b) # 30
print("division",a/b) # return the qu  3.3333333333333335
print("modulus",a%b) #modulo division 
print("floor division", a//b)   # return 3
print("exponential", a**b) # 10*10*10


# Assignment:
x=10
x+=10 

x=x+10 
x=10+10 


y=50
y+=100
print(y)


z=5 
z*=10   
print(z)

3. comparision operator 

a=15
b=10
print(a!=b)
print(a>=b)

print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b) 

4. Logical operator: 
------------ 

used to combine multiple condition

and - both condition must be true
or - true if atleast one condition is true 
not - reverse the result


a=10
print(a>20 and a<25 ) # F =>F
print(a>5 and a<20) # T and T => T
print(a>5 and a<7) # T and F => F 
print(a>30  and a<50) #  F => F 


or  any T 

a=10
print(a>20 or a<25 ) # F T => T
print(a>5 or a<20) # T or T => T 


not 

a=10
print(not a>5)  # F => 


print(10 and 0)
print(0 and 10)

# 5.identity operator
is  - Same object
is no  - different object

used to check whether two variale refer to the same object in memory  

a=10
b=10
print(id(a))
print(id(b))

print(a is b)


a=10.5 
b=11.5 
print(id(a))
print(id(b))

print(a is b)

a=[10,20,30]
b=[10,20,30]
b.append(40)
print(id(a))
print(id(b))

print(a is b)


a=[10,20,30]
b=a
print(id(a))
print(id(b))

print(a is b)


a=[10,20,30]
b=a.copy()
print(id(a))
print(id(b))

print(a is b)
print( a is not b)


# 6. membership operator

in - checks whether the value exists
not in  checks whether the value does not  exists

a=[10,20,30,40,50]

print(20 in a)
print(90 in a)


print(20 not in a)


7 bitwise operator

(& - and )
| - or 
^ -xor 
~ - not 
>> right shift
<< left shift

- used to perform binary operations 


a=5 
b=3 

print(bin(5)) # 0b101 
print(bin(3)) # 0b11 

print( a&b )

a=4
b=2
print( a|b )

print(~b)

4=> 0100
2=> 0010
---------
    0110
or











