# list methods:
 # mutable, ordered,allow duplicate, hetrogenous 

# add values in list 
1. append 
2. extends
3. insert 

1. append()
1. add only one element at a time 
2. add element at the end of the list 
3. it modifies original 
4. it does not return the updated list


a=[1,2,3]

print(type(a)) 

a.append(4)
a.append([5,6])


print(a)

a=[1,2,3]
b=[4,5,6]

a.extend(b)

c=['A','B']
c.extend("cde")
print(c)



3. insert()

a=[1,2,3,4,5]

a.insert(2,9)

print(a)


Remove value from the list 
1. remove() --  remove based on the value 
2. pop() -- based on index position 

a=[1,2,3,4,5]

a.remove(3)
print(a)

a=[1,2,3,4,5]
a.pop()
print(a)
a.pop(1)
print(a)

a.pop(5)  # IndexError: pop index out of range

del keyword

a=[1,2,3]
print(a)
del a
print(a) # NameError: name 'a' is not defined 

a=[10,20,30,40,50]
del a[1:4] 
print(a)


clear()


a=[10,20,30]
a.clear()
print(a)


count() -> count the occurence

a=[10,10,10,20,30,30,30]
print(a.count(10))

sort()
- arrange elements in order 

number=[50,10,40,20,30]
number.sort()
print(number)
number.sort(reverse=True)
print(number)

a=["apple","orange","banana","pineapple","cherry","grape","fig"] 
a.sort(key=len)
print(a)
a.sort()
print(a)
a.sort(reverse=True) 

reverse 

a=["apple","orange","banana","pineapple","cherry","grape","fig"] 
# a.reverse()
# print(a)

print(a.index("bananaaa")) # ValueError: list.index(x): x not in list 

a=[1,2,3,4,5] 
b=a 
b.append(6)
print(b)
print(a) 
print(id(a))
print(id(b))

a=[1,2,3,4,5] 
c=a.copy()
print(c)

print(id(a))
print(id(c))

c.append(6)
print(a)
print(c)


Tuple:
#- immutable 
a=(1,2,3,4,5)


set method 
# mutable
# unordered 

a={1,2,3}
a.add(4)
print(a)
a.clear()
print(a)

a=set()
print(a)

union - unique no from both set 
intersection - element which contain in both 
difference - 

a={1,2,3} 
b={2,3,4}
print(a.union(b)) # {1, 2, 3, 4} 
print(a | b) 

print(a.intersection(b)) 
print(a & b) 

print(a.difference(b))
print(a-b)
print(a.symmetric_difference(b))
print(a ^ b)  


# dict: 
# ----- 

a={
    "name":"apple",
    "color":"red"
}
print(a)
print(type(a))

a['price']=120 
print(a)

a['color']="green"
print(a)

print(a.keys())
print(a.values())
print(a.items())





