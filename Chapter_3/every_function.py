games = ['rpg', 'fps', 'moba', 'strategy', 'adventure', 'simulation', 'sports']
print(games)

print(games[3])
print(games[1].title()) # Capitalizing the second element
print(games[-1])
message = f"My favorite game genre is {games[1].title()}" # Creating a message
print(message)
games[0] = 'action' # Changing the first element
print(games)

games.append('horror') # Adding an element to the end
print(games)

games.insert(2, 'puzzle') # Inserting an element at index 2
print(games)

del games[6] # Deleting the element at index 6
print(games)

popped_games = games.pop(-1) # Popping the last element
print(games)

print(popped_games) # Displaying the popped element
print(f"The least played game genre I play {popped_games.title()}")
most_played = games.pop(1) # Popping the element at index 1
print(f"The most played game genre is {most_played.title()}")
print(games)

games.remove('adventure') # Removing the element 'moba'
print(games)

too_hard = 'moba' # Assigning 'moba' to a variable
games.remove(too_hard) # Removing the element stored in the variable
print(games)

print(f"\nA {too_hard.title()} game is too hard for me to enjoy.")
games.sort() # Sorting the list permanently in alphabetical order
print(games)

games.sort(reverse=True) # Sorting the list permanently in reverse alphabetical order
print(games)

print("\nHere is the original list:") # Displaying the original list
print(games)

print("\nHere is the sorted list:") # Displaying the sorted list without modifying the original
print(sorted(games))

print("\nHere is the original list again:") # Displaying the original list again
print(games)

print(games)
games.reverse() # Reversing the order of the list
print(games)

len(games) # Finding the length of the list
print(len(games))
