def palindrome(a):
     a = a.replace(" ", "").lower()
     return a == a[::-1]
user_input = input("Enter a string: ")
if palindrome(user_input):
          print("Yes, your string is a palindrome!")
else:
          print("Sorry, your string is not a palindrome.")