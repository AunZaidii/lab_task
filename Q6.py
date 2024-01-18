dog=set(range(1,84))
cat=set(range(47,148))
fish=set(range(72,78))|(set(range(138,154)))|set(range(1,9))
other=set(range(155,189))
onlydog=dog-(cat|fish)
onlycat=cat-(dog|fish)
onlyfish=fish-(dog|cat)
total=dog|fish|cat|other
onlycatndog=(cat&dog)-fish
onlycatnfish=(cat&fish)-dog
onlydognfish=(dog&fish)-cat
allthree=cat&fish&dog
print("{:^40}".format("THE GIVEN DATA"))
data={"dog product":len(dog),"cat product":len(cat),"fish product":len(fish),
      "a cat and a dog product":len(onlycatndog),"a dog and a fish product":len(onlydognfish),
      "a cat and a fish product":len(onlycatnfish),"a cat, a fish and a dog product":len(allthree),
      "a product other than a cat, dog and a fish product":len(other)}
for i,j in data.items():
    print("People who purchased",i,"=",j)

print("{:^40}".format("ANSWERS"))
print("People who purshased only dog product:",len(onlydog))
print("People who purshased only cat product:",len(onlycat))
print("People who purshased a dog or a fish product:",len(onlyfish|onlydog))
print("Total purchases=",len(total))
