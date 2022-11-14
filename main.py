pi = 4
x = 3
i = 0
while True:
    pi -= 8/(x*(x+2))
    x += 4
    i += 1
    if i == 10_000_000:
        print(pi)
        i = 0
