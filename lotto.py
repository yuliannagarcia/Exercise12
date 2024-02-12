import random

# random = a built-in Python module that provides functions for generating random numbers.

# generating 6 unique random lottery numbers between 1 and 50
lottery_no = set()
# initializes an empty set called lottery_no.
while len(lottery_no) < 6:
    # enters a while loop that continues as long as the length of lottery_no is less than 6
    generated_no = random.randint(1, 50)
    # random.randint(a, b) is a function provided by the random module in Python. It generates a random integer between
    # the two specified integers a and b. a = lower-bound range and b upper-bound range
    # generates a random integer between 1 and 50
    lottery_no.add(generated_no)
    # the random generated number is added to the lottery_no set using add() method
    # sets don't allow duplicate elements, only unique random numbers are added to the set

# Display the generated lottery numbers
print("Lottery numbers:")
for number in lottery_no:
    print(number)

#  the code prints them out one by one. the for loop iterates over each element (num) in the lottery_numbers set.
