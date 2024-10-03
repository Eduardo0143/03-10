def coiso(n):
    x = n -1 
    while x > 2:
        if (n % x) == 0:
            return True
        else:
            x = x - 1


n = int(input("Insira número"))

print(coiso(n))