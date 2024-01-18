a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
if 2*a == 0:
    print("The equation cannot solve as there is a zero division.")
else:
    ans1=(-b + ((b**2) - (4*a*c))**0.5) / (2*a)
    ans2=(-b - ((b**2) - (4*a*c))**0.5) / (2*a)
    print(ans1,ans2)