if __name__ == '__main__':
    #now create a empty dictionary
    sheet={}
    #the for loop will add the names and score to the dictionary with the name as the key and the score as the value
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sheet[name]=score
    #created another list 
    values=sheet.values()
    secondsmallest=sorted(set(values))[1]
    print(secondsmallest)
