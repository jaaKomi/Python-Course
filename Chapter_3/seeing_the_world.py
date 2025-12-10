locations = ['Las Vegas', 'Amazon', 'Hawaii', 'Caribbean', 'Tokyo']
print(locations)
print(sorted(locations))  # Temporary alphabetical sort
print(locations)  # Original list remains unchanged
print(sorted(locations, reverse=True))  # Temporary reverse alphabetical sort
locations.sort()
print(locations)  # Permanently sorted in alphabetical order
locations.sort(reverse=True)
print(locations)  # Permanently sorted in reverse alphabetical order
