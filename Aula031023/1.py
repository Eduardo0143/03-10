def quo(a,b,c):

    x = (-b + ((b**2-4*a*c)**0.5))/2*a
    y = (-b - ((b**2-4*a*c)**0.5))/2*a
 
    return(x,y)


a = int(input("Quoeficiente a: "))
b = int(input("Quoeficiente b: "))
c = int(input("Quoeficiente c: "))

print(quo(a,b,c))





