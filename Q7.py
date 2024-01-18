students=set(range(1,111))
eng=set(range(1,76))
span=set(range(1,14))|set(range(56,95))
fren=set(range(86,106))|set(range(1,14))|set(range(14,31))
onlyengnspan=(eng&span)-fren
onlyengnfren=(eng&fren)-span
onlyfrennspan=(fren&span)-eng
neither=students-(eng|span|fren)
allthree=eng&fren&span
onlyfren=fren-(eng|span)
onlyspan=span-(eng|fren)
onlyeng=eng-(span|fren)
print("{:^40}".format("GIVEN DATA"))
data={"only English":len(onlyeng),"only Spanish":len(onlyspan),"only French":len(onlyfren),
      "only English and Spanish":len(onlyengnspan),"only English and French":len(onlyengnfren),
      "only French and Spanish":len(onlyfrennspan),"all English, Spanish and French":len(allthree)}
print("Total Students =",len(students))
for i,j in data.items():
    print("Students who speak",i,"=",j)
print("{:^40}".format("ANSWERS"))
print("Students who speak English and Spanish but not French:",len(onlyengnspan))
print("Students who speak neither English, Spanish nor French:",len(neither))
print("Students who speak French, but neither English nor Spanish:",len(onlyfren))
print("Students who speak only one of the three languages:",len(onlyfren|onlyeng|onlyspan))
print("Students who speak exactly two of the three languages:",len((onlyengnfren|onlyfrennspan|onlyengnspan)-allthree))
