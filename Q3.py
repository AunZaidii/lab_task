import os
def duplicate(filename):
    f=open(filename,"r")
    content=f.read()
    f.close()
    word_list=content.split()
    for i in range(len(word_list)):
        if word_list[i] in word_list[i+1:]:
            print(True)
            break
    else:
        print(False)
duplicate('C:\programming.txt')
