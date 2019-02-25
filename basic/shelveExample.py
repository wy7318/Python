import shelve

with shelve.open('ShelfTest') as fruit: #with method automatically close
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)

#shelve is persistant to file
