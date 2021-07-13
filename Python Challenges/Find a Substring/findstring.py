def count_substring(string, sub_string):
    mainstr=list(string)
    substr=list(sub_string)
    nummatch = 0

    for itrstr in range(0,len(mainstr)):
        if substr[0] == mainstr[itrstr]:
            itrsub = 0
            for itrsub in range(0, len(substr)):
                if substr[itrstr] != mainstr[itrsub+itrstr] and itrstr + itrsub:
                    break
                else:
                    nummatch = nummatch + 1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)