def count_substring(string, sub_string):
    nummatch = 0

    for itrstr in range(0,len(string)):
        if string[i:].startswith(substring):
            nummatch += 1

    return nummatch
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
