welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company","Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda ="More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
imelda = imelda[0], "Imelda May", imelda[2] #assigning new element
#Tuple cannot assign value through string
print(imelda)

metallica2 =["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] ="Master of Puppets" #In the case of list, we can assign new value right away
print(metallica2)

#==============================================================================

a = b = c =12
print(c)
a, b = 12, 13
print(a, b)
a, b = b, a
print(a, b)
