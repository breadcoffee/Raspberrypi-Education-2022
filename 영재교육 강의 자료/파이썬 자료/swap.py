def swap(a, b):
    a,b = b,a
    return a,b

a,b=5,10
print(a,b)
a,b=swap(a,b)
print(a,b)
