print("Content that you wanna print on screen")
#output
var1 = "Shruti"
print("Hi my name is: ",var1)
#input from users
var1 = input("Enter your name: ")
print("My name is: ", var1)
#typecasting input
var1=int(input("enter the integer value"))
print(var1)

var1=float(input("enter the float value"))
print(var1)

#range functions
#range(int_start_value,int_stop_value,int_step_value)

for i in range(0,101,2):
    print(i)

for i in range(0,101,1):
    print(i)

for i in range(0,101,3):
    print(i)

#octal numbers
print("\ooo")

#string ,it can be used by both type of quotation single quotes and double quotes
str="Shruti"
print("string is ",str)

#indexing
#The position of every character placed in the string starts from 0th position ans step by step it ends at length-1 position

#slicing
str[1:5]
print(str[1:5])


#list
#list is mutable,ordered,indexed(oth to length-1  position),and most flexible and dynamic collection of elements in python

my_list = ['apple', 'mango' , 'orange' ]
#return the first element of list
print(my_list[0])

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Creating a mixed list with different data types
mixed_list = [10, "hello", 3.14, True, "world"]

# Accessing elements of a list using indexing
print(numbers[0])  # Output: 1
print(fruits[2])   # Output: "orange"
print(mixed_list[3])  # Output: True

# Modifying elements of a list
numbers[1] = 20
fruits[3] = "pineapple"
mixed_list[0] = "updated"

print(numbers)  # Output: [1, 20, 3, 4, 5]
print(fruits)   # Output: ["apple", "banana", "orange", "pineapple", "kiwi"]
print(mixed_list)  # Output: ["updated", "hello", 3.14, True, "world"]

# List concatenation
combined_list = numbers + fruits
print(combined_list)  # Output: [1, 20, 3, 4, 5, "apple", "banana", "orange", "pineapple", "kiwi"]

# List slicing
sliced_list = combined_list[2:6]
print(sliced_list)  # Output: [3, 4, 5, "apple"]

# List length
print(len(numbers))  # Output: 5
print(len(fruits))   # Output: 5

# Adding elements to a list
fruits.append("mango")
print(fruits)   # Output: ["apple", "banana", "orange", "pineapple", "kiwi", "mango"]

# Removing elements from a list
numbers.remove(3)
print(numbers)  # Output: [1, 20, 4, 5]



