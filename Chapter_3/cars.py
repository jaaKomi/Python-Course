cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #this will sort the list in alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #this will sort the list in reverse alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) #this will sort the list temporarily
print("\nHere is the original list again:")
print(cars) # the original list is unchanged

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #this will reverse the order of the list
print(cars)
cars.reverse() #reversing again to get back the original order
print(cars)

print(len(cars)) #this will print the length of the list
