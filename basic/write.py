cities = ["Adelaide", "Alice Springs", "Seoul", "Melbourne", "Sydney"]

with open("/Users/vazzo/Desktop/python/cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file) #Create txt file

print("Adelaide".strip('A')) #deleting 'A' and print leftover

#=================================append into txt=============================================

with open("/Users/vazzo/Desktop/python/sample.txt", 'a') as tables: #append times table
    for i in range(1,13):
        print("{} times {} is {}".format(i, 2, 1*2), file=tables)
