# Loop 
-   It execute a block of code repeatedly 
- until given condition is satisfied


print("welcome")
print("welcome")
print("welcome")
print("welcome")
print("welcome")
print("welcome")
print("welcome")

Notes: 
1. reduce code repetation 
2. make code easier to maintain 
3. save development time


Type of loop 
    1. for loop 
    2. while loop 


for loop:
----------
    -  iterate over collection 
    - example : str,list,tuple,set,dict 

Syntax: 

for variable in sequence : 
    statement 

fruits=["Apple","Orange","Banana","Grapes"]

for i in fruits:
    print(i)

step 1: 

i= "Apple"
    # Apple 

i="Orange"
    # "orange"

i="Banana"
    # Banana 

Syntax: range(start,end,step ) 


for i in range(1,11): #[1,2,3,4,5,6,7,8,9,10]
    print(i)

for i in range(1,11,2): #[1,2,3,4,5,6,7,8,9,10]
    print(i)

for i in range(1,11,3): #[1,2,3,4,5,6,7,8,9,10]
    print(i)


veg="brinjal"
for c in veg:
    print(c)


num=123
for i in num:
    print(i)


students=("Mohansai","Shyam","Nithila")
print("Loop Example")
for m in students:
    print(m)
    print("welcome")
print("Completed")

# add values from 1 to 5


total=0
for i in range(1,6):
    total+=i 
print(total)

iteration1: 
    total =0 i=1 total=1 
iteration 2 : 
    total=1 i=2 total=3

While loop 
---------- 
    Executes a block of code  as long as condition is true 

# Syntax: 
#     while condition:
#         statement 


i=1 
while i<=5:
    print(i)
    i+=1

i=10
while i>=5:
    print(i)
    i-=1

num = 5
i=1 
while i<=10:
    print(f"{num} * {i} = {num*i}")
    i+=1

Nested Loop 
------------
    loop inside another loop 


for i in range(1,4): # [1,2,3]
    for j in range(1,4): # [1,2,3]
        print(f"({i},{j})",end=" ")
    print()

(1,1) (1,2) (1,3) 
(2,1) (2,2) (2,3) 
(3,1) (3,2) (3,3)

itera 1: 
outer loop i=1 
    inner loop j=1 
        # 1,1
    inner loop j=2 
        # 1 2
    inner loop j=3 
        # 1 3
outer loop i=2 
    inner loop j=1 
        # 2 1
    inner loop j=2 
        # 2 2 
    inner loop j=3 
        # 2 3 
outer loop i=3 
    inner loop j=1 
            # 3 1
        inner loop j=2 
            # 3 2 
        inner loop j=3 
            # 3 3  


for i in range(1,4): # [1,2,3]
    for j in range(1,4): # [1,2,3]
        print("*",end=" ")
    print()   


111
222
333

for i in range(1,4): # [1,2,3]
    for j in range(1,4): # [1,2,3]
        print(i,end=" ")
    print() 

123
123
123

for i in range(1,4): # [1,2,3]
    for j in range(1,4): # [1,2,3]
        print(j,end=" ")
    print() 


for i in range(2):
    print(i)


for i in range(1,4): #[1,2,3]
    for j in range(i): #[0]  [0,1] [0,1,2]
        print("*",end=" ")
    print()



step 1: 
i =1 
    j=0  * 
i=2 
    j=0 * *
    j=1 
i=3 
    j=0 * * *
    j=1 
    j=2

1
12
123

for i in range(1,4):
    print("*"*i)
    

a="3"
print(a*5)

a=[1,2,3,4]
print(a*2)


A 
AB 
ABC 


ASCII - American Standard code for information interchange

chr()
ord()


print(chr(65+0))
print(ord('a'))


for i in range(1,4): #[1,2,3]
    for j in range(i): #[0]  [0,1] [0,1,2]
        print(chr(65+i),end=" ")
    print()

A 
AB 
ABC 




# 1 nithila
# 2 shyam 
# 3 sai 


a= ['nithila','shyam','sai']
counter=1
for i in a:
    print(counter,i)
    counter+=1

enumerate()

a= ['nithila','shyam','sai']
for i,v in enumerate(a,start=1):
    print(i,v)

zip ()

a= ['nithila','shyam','sai']
b= ['chennai','bangalore','Hydrabad','Andra']
c= [99,99,98]

# print(a+b+c)

print(zip(a,b,c))

print(list(zip(a,b,c)))


iterator: 

1. iter()
2. next()

a=[1,2,3,4,5]

res=iter(a)
print(next(res))
print(next(res))

# generator 

# 1. yield()
# 2. next()

1. break   # break the loop
2. continue  # skip the current Iteration
3. pass 

for i in range(1,10):
    if i == 5:
        print("i am ten")
        break
    print(i)
else:
    print("Loop ends here")
print("Loop ended")

for i in range(1,10):
    if i == 5:
        print("i am ten")
        
    print(i)
else:
    print("Loop ends here")
print("Loop ended")



for i in range(1,10):
   
    if i == 5:
        continue
    print(i)   

pass 

for i in range(1,4):
    pass

print("welcome")



1. find even numbers in list  
2. remove duplicate from list 
3. sum the odd numbers in list 
4. find vowels in str 
5. count the vowels and consonents

