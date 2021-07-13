import sys
def swap_case(s):
    newstring = list(s)
    for letter in range(len(newstring)):
        if newstring[letter].isupper():
            newstring[letter]=newstring[letter].lower()
        elif newstring[letter].islower():
            newstring[letter]=newstring[letter].upper()
    return "".join(newstring)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)