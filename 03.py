#coding: utf-8

# Day 3: Lists in Python
# A long flight is an excellent time for reflection and meditation, and Dot couldn’t wait to settle into their seat and rest. The plane was huge, with hundreds of seats, rows and rows of them stretching down the long aisles. Dot glanced down at their ticket to see which of the seats belonged to them. Just at that moment, another passenger in the aisle stumbled and knocked right into Dot. “Oh dear, I apologize, fellow flyer!” the passenger says, “sometimes I just can’t seem to get my bearings, stumbling every which way! I hope I did not disturb you too intensely.” Dot smiled and reassured the odd woman, clarifying that they weren’t harmed.

# Dot looked back towards their ticket — oh no! It seemed that Dot spilled some of their coffee on the slip of paper during the hubbub. There was a dark wet spot right over where the seat number was supposed to be. Dot looked up and down the plane and saw that most of the seats were already occupied by passengers. They need to find their seat quickly before the plane takes off — let’s use our data skills to help them verify their seat number.


# Challenge
# We need to find Dot an empty seat on the plane. We have logged the layout of the section of the plane as a Python list. This is formatted as a nested list, which means that elements of the list are lists as well. Listception.

# Note: Our plane section contains three sections of seats in each row, and three seats in each section. Here is what the values in the layout mean:

# e = empty seat
# o = occupied seat
# None = aisle (you can't sit here!)
# Capital letters = window seats
layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]
# Dot has two conditions for their sitting:

# It has to be window seat
# The next seat needs to be empty
# Identify the right place for Dot to sit. If there is more than one option that matches the conditions above, choose the seat that is closer to the front, i.e. has a lower row number. What is the list index of Dot's seat?

print (layout[3][-1])

# Stretch Question
# Use python's pop() and insert() list functions to change Dot's seat from E to O.

# Stretch Questions are not required to be completed to finish the challenge but are recommended to further develop your skills.

layout[3][-1] = 'O'
print(layout)