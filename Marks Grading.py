a = input("Enter your name: ")
marks = float(input("Enter your marks out of 100: "))
if marks>=80 and marks<100:
    print(a+",","You have secured A+ grade")
elif(marks>=70 and marks<80):
     print(a+",","You have secured A grade")
elif(marks>=60 and marks<70):
      print(a+",","You have secured B grade")
elif(marks>=50 and marks<60):
 print(a+",","You have secured c grade")
elif(marks<50):
    print(a+",","You have failed in your exam")
else:
     print(a+",","You have entered invalid marks")


