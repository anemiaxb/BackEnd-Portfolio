"""
Date: 3/19/2020
Version: uDemy Course: https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/
Owner: Jose Portilla
Author: anemiaxb
Rationale:
"""

print('#1')  # What is 7 to the power of 4?
result = 7 ** 4
print(result)

print('------' * 20)

print('#2')  # Split this string into a list: 'Hi there Sam!'
s = 'Hi there Sam'
s.split()
print(s)

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print('#3')  # Given the variables, use .format() to print the following string: The diameter of Earth is 12742 kilometers.

planet = "Earth"
diameter = 12742

print('The diameter of {} is {} kilometers'.format(planet, diameter))

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print('#4')  # Given this nested list, use indexing to grab the word "hello"

lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

print(lst[3][1][2][0])

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print('#5')  # Given this nested dictionary grab the word "hello".

d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

# 6 What is the main difference between a tuple and a list?
# A tuple is immutable and a list is mutable.

print('#7')  # Create a function that grabs the email website domain from a string in the form: user@domain.com


def domainGet(email):
    return email.split('@')[1]


print(domainGet('user@domain.com'))

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print(
    '#8')  # Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a


# punctuation being attached to the word dog, but do account for capitalization.


def findDog(text):
    return 'dog' in text.lower().split()


print(findDog('Is there a dog here?'))

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print('#9')  # Create a function that counts the number of times the word "dog" occurs in a string.


def countDog(string):
    count = 0
    for word in string.lower().split():
        if word == 'dog':
            count += 1
    return count


print(countDog('This dog runs faster than the other dog dude!'))

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print('#10')  # Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.

seq = ['soup', 'dog', 'salad', 'cat', 'great']

print(list(filter(lambda word: word[0] == 's', seq)))

# ------------------------------------------------------------------------------------------------------------------------
print('------' * 20)
# ------------------------------------------------------------------------------------------------------------------------

print('#11')
'''
You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", 
"Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is 
"Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of 
the function) -- on your birthday, your speed can be 5 higher in all cases.
'''


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(caught_speeding(90,True))