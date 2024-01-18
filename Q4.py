monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsL.insert(3, 'Apr')

monthsT = ('Jan', 'Feb', 'Mar', 'May') 

monthsL.append('Jun')
monthsT = monthsT + ('Jun',)

popped_element_L = monthsL.pop()

del monthsL[1]
monthsT = monthsT[:1] + monthsT[2:]

monthsL.reverse()
monthsT = tuple(reversed(monthsT))

print("List after inserting 'Apr':", monthsL)
print("Tuple after attempting to insert 'Apr':", monthsT)
print("List after appending 'Jun':", monthsL)
print("Tuple after appending 'Jun':", monthsT)
print("Popped element from the list:", popped_element_L)
print("List after removing the second item:", monthsL)
print("Tuple after attempting to remove the second item:", monthsT)
print("List after reversing:", monthsL)
print("Tuple after reversing:", monthsT)

