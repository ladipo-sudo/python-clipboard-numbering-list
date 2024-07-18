#! python3
# ascendingNumberAdder.py - Adds numbers in ascending order to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

#seperate lines and add stars
lines = text.split('\n')
counter = 1
for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = f"{counter}. {lines[i]}"#add number with dot to each string in "lines" list
    counter += 1 # Increment counter for next line
text = '\n'.join(lines)
pyperclip.copy(text)