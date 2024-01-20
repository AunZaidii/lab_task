provinces_tuple = ()
num_provinces = int(input("Enter the number of provinces: "))

for i in range(num_provinces):
    province_name = input(f"Enter the name of province {i+1}: ")
    provinces_tuple += (province_name,)
print("Provinces Tuple:", provinces_tuple)

