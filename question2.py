'''
1. The variable changed is a reference to the string s which has already been initialised.Strings are
immutable,therefore it is not possible to change elements in a string once initialised. It is however possible
to concatenate which creates a new string (i.e. assigning a new string to the same variable name). To fix, initialise
changed to an empty string and concatenate the characters in the for loop.
2. The range of the for loop is incorrect resulting in the code not processing the last character of the loop.
The loop will index up to the second parameter minus 1. So the second for loop parameter should be len(s),
not len(s) -1.
'''


def replace(s):
    changed = ""
    for i in range(0, len(s)):
        if s[i]>='a' and s[i]<='z':
            changed += s[i].upper()
        else:
            changed += s[i]
    return changed

print(replace("RiChArD"))
