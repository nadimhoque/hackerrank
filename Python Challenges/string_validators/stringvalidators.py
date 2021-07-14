if __name__ == '__main__':
    
    s = input()
    #I used the any returns true if any of the is* are true in the string
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
