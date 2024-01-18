import os
def abc(filename):
    f = open(filename,"r+")
    content = f.read()
    f.close()
    f1 = open('D:\\er.txt', "a")
    word_list=content.split()
    for i in range(len(word_list)):
        if len(word_list[i]) == 4:
            word_list[i] = "XXXX"
    f1.write(" ".join(word_list))
    f1.close()
abc('D:\\programming2.txt')