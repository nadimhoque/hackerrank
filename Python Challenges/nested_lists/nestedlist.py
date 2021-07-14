if __name__ == '__main__':
    #now create a empty dictionary
    sheet={}
    
    #the for loop will add the names and score to the dictionary with the name as the key and the score as the value
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sheet[name]=score
    
    #created another list that contains just the grades
    values=sheet.values()
    
    #I am going to convert the list to a set so that all duplicates are removed. Then I will sort this list so it is in ascending order. Because
    #there are nore repeats I can assume that the second item is the second largest number
    secondsmallest=sorted(set(values))[1]

    #create a empty list so that we can sort it later
    names = []
    #go through the dictionary. if the value matches the second highest score, append it to the names list
    for key,value in sheet.items():
        if value == secondsmallest:
            names.append(key)
    
    #sort the names list so the names are alphabetical
    names.sort()
    #the for loop then prints all of the names one line at a time
    for i in names:
        print(i)
