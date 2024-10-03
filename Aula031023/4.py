def fat(n):
    if n <= 1:
        return 1
    else:
        return n * fat(n-1)


n = int(input("Insira n: "))
print(fat(n))
