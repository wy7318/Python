cities = ["Adelaide", "Alice Springs", "Seoul", "Melbourne", "Sydney"]

with open("/Users/vazzo/Desktop/python/cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file) #Create txt file

print("Adelaide".strip('A')) #deleting 'A' and print leftover
