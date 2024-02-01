def count(n, x):
    result = 0
    ls = []
    for i in range(1, n+1):
        m = i
        if m % 10 == x:
            ls.append(m)
            result += 1
    print(result)
    print(ls)

count(1000, 8)
