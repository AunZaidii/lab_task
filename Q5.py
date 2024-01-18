monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')
monthsL.insert(3, 'Apr')
monthsL.append('Jun')
popped_element_L = monthsL.pop()
del monthsL[1]
monthsL.reverse()
print("(a) List after inserting 'Apr':", monthsL)
print("(b) List after appending 'Jun':", monthsL)
print("(c) Popped element from the list:", popped_element_L)
print("(d) List after removing the second item:", monthsL)
print("(e) List after reversing:", monthsL)

