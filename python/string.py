# string : collection characters enclosed within quotes

String :Immutable ( cannot modify after its created )


name ="python"
# upper() 
name=name.upper() 
print(name)

to convert into Lowercase 

lower()

name="PYTHON programming"
print(name.lower())

print(name.capitalize())
print(name.title())


Removing Space 

strip  - removes space from both begining and Ending 
lstrip - removes space from beginition
rstrip - removes space at the end 


name = " python "
print(name.strip())
print(name.lstrip())
print(name.rstrip())


3. Searching Methods: 
- search paticular character or word inside a string 

1. find() - find index position of the character 
2. index() - find and return the index position


# Syntax: string.find(value,start,end)


a= "Python Programming"
print(a.index('P'))
print(a.index('p'))

print(a.find('z'))

print(a.find("P"))
print(a.find("Programming"))
print(a.find('n'))
print(a.find('o',6,9)) # 6,7,8


count - no of occurance

a="banana"
print(a.count('a'))
print(a.count("ana")) 

a="python is programming Languague. python is easy to learn"
print(a.count("python"))


replace: 

string.replace(old,new,count) 

a="i like python, python is Easy , python is Simple to understand"
print(a.replace("python","java")) 
print(a)
print(a.replace("java","python"))

a="banana"
print(a.replace('a','o'))
print(a.replace('a','o',2)) # it only replace limited number of occurance

# String Checking

1. isalpha() => checks whethere all the character are alphabet 

name="shyam"
print(name.isalpha())

name="shyam123"
print(name.isalpha())

name="Nithila "
print(name.isalpha())

name=""
print(name.isalpha())


num="120"
print(num.isdigit())

num="120abs"
print(num.isdigit())



