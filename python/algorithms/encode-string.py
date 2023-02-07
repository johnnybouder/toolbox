import string

Number2Letter = {}
Letter2Number ={}

# Make both dictionaries
for i, letter in enumerate(string.ascii_lowercase):
    Number2Letter[i] = letter
    Letter2Number[letter] = i

s1 = 'the lazy dog jumped over the quick brown fox'
print(s1)
# Encode the string!
s2 = ''
for letter in s1:
    if letter in Letter2Number:
        current_letter_number = Letter2Number[letter] + 2

    # take care of the edge cases 
    if current_letter_number == 26:
        current_letter_number = 0
    elif current_letter_number == 27:
        current_letter_number = 1
        s2 += Number2Letter[current_letter_number]
    else:
        s2+=letter

print(s2)