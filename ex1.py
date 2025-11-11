def add(a,b):
    c = a+b
    print(c)
add(2,3)    
c = input("enter value")
d = input("enter value")
add2 = int(c)+int(d)
print("addition of c and d is".format(c,d,add2),add2)


print("looping statements")
e = 50
f = 100
if (e>f):
    print("a is greater than b")
else:
    print("b is greater than a")

print("while loop")

i=0
while(i<10):
    print(i)
    i+=1

print("for loop")
for i in range(10):
    print(i)

print("function")
def print_num():
    for i in range(10):
        print(i)

print_num()        

print("file handling")
file = open('introduction.txt','r')
print(file.read())
file.close()
