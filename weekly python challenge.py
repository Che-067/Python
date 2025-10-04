# Tasks: 

# These tasks should test your understanding of basic concepts related to
#  lists, tuples, dictionaries, and sets in Python. Good luck!


# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

#collect = float(input('Enter your number: '))

#narendra = float(input('Enter your number: '))

#merger = float(input('Enter your number: '))

#brass = float(input('Enter your number: '))

#array = []

#array.append(collect)

#array.append(narendra)

#array.append(merger)

#array.append(brass)

#total = round(sum(array),3)

#print(f'The total is : {total}')


# create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.

#books = ('Guerilla warfare','A MUST UNITE','LOST VICTORIES','THE CASE FOR ISLAM',"OSMAN'S DREAM")

#for fruit in books:
#  print(fruit)


  # Write a program that uses a dictionary to store information about a person,
#  such as their name, age, and favorite color. Ask the user for input and store
#  the information in the dictionary. Then, print the dictionary to the console.

#name = input('Enter your name: ')

#age = input('Enter your age: ')

#favorite_color = input('Enter your color : ')

#dictionary = {
#  'name' : name,
# 'age' : age,
  #'favorite_color' : favorite_color
#}

# print(dictionary)


# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
input1 = input('Enter set1 value: ')

input2 =  input('Enter set1  value: ')

input3 =  input('Enter set1  value: ')

input4 =  input('Enter set1  value: ')

input5 =  input('Enter set2 value: ')
input6 =  input('Enter set2 value: ')
input7 =  input('Enter set2 value: ')
input8 =  input('Enter set2 value: ')

set1 = set()
set1.update({input1,input2,input3,input4})

set2 = set()

set2.update({input5,input6,input7,input8})

set3 = set1 & set2

print(f'The common elements are: {set3}')

# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list 
# that contains only the words that have an odd number of characters.

var = [44,32,57,5,21,90]
odd_numbers = [x for x in var if x % 2 != 0 ]

print(odd_numbers)