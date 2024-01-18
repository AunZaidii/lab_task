def tn():
    a=int(input("Enter first term: "))
    d=int(input("Enter common difference: "))
    nth=int(input("Enter the term you want to calculate: "))
    ans=a+(nth-1)*d
    print(ans)
    key=input("Do you wish to continue? Yes Or No ")
    key=key.lower()
    if key=="yes":
        return tn()
tn()