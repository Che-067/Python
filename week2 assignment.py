
# Create an empty list called my_list.
my_list = []

#Append the following elements to my_list: 10, 20, 30, 40.

my_list.append(10)

my_list.append(20)

my_list.append(30)

my_list.append(40)

print(my_list) # output [10, 20, 30, 40]

#Insert the value 15 at the second position in the list.

my_list[1] = 15

print(my_list)

# extend my_list with another list: [50, 60, 70].

another_list = [50, 60, 70]

my_list.extend(another_list)

print(my_list)

#Remove the last element from my_list.

del my_list[(len(my_list) - 1)]

print(my_list)

#Sort my_list in ascending order

my_list.sort()

print(my_list)

# Find and print the index of the value 30 in my_list

for language in my_list:
  if language == 30:
    index = my_list.index(30)
    print(index)

