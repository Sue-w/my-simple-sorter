# This app simply sorts a list of random numbers and returns the sorted list as output
# The list is initially generated randomly but later asks the user to enter a random number list of their own

# Importing the random number generating package
import random

random_list = []
for i in range(0, 10):
    n = random.randint(1, 100)
    random_list.append(n)

random_list1 = []
for i in range(0, 10):
    n = random.randint(1, 100)
    random_list1.append(n)

random_list2 = []
for i in range(0, 10):
    n = random.randint(1, 100)
    random_list2.append(n)

print("Hello. \n I am Simple Sorter. I simply sort a list of random numbers."
      " \n \n Like this: \n ")
print(f"Unsorted List= {random_list}  \n Sorted List= {sorted(random_list)} \n \n or like this: \n \n"
      f"Unsorted List= {random_list1} \n Sorted List= {sorted(random_list1)} \n \n or like this: \n \n"
      f"Unsorted List= {random_list2} \n Sorted List= {sorted(random_list2)} \n \n")

print("That's all folks, have a good day!")
