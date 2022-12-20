print("1. Write a Python program to print 'Hello Python'?")
a="Hello"
b="Python"
while len((a))<len(b):
    print(a+ "",b)
    break

print("2. Write a Python program to do arithmetical operations addition and division.?")
def add(a,b):
    z=a+b
    return z
print(add(2,3))


def mul(v,c):
    x=v*c
    return x
print(mul(3,4))

print("3. Write a Python program to find the area of a triangle?")
def ar(a,b):
    print("Area of trianle is ")
    f=(1/2)*(a*b)
    return f
print(ar(2,4))

print("5. Write a Python program to generate a random number?")

print(list(range(7)))
