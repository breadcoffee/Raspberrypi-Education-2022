def odd(ls):
    for x in ls:
        if x % 2 == 1:
            print(x)

def even(ls):
    for x in ls:
        if x % 2 == 0:
            print(x)

ls = [1,2,3,4,5,6,7,8,9]
print("Odd")
odd(ls)
print()
print("Even")
even(ls)
