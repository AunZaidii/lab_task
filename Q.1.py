
def check(x):
    y = []
    for i in range(0, x):
        if x%(i+1)==0:
            y.append(i+1)
    print(y)        
check(int(input("enter number: ")))
        


