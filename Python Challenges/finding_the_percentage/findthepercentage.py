if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #I have put the grades of the select user into the list called grades
    grades = student_marks[query_name]
    
    #I used the sum() to have python add all the contents of the grades list, then I divided by the length of the list. Technically I could have used 3 but this code is a bit more flexible especially because the input has no restriction on how many the user can enter for the grades
    avg=sum(grades)/len(grades)

    print(format(round(avg,2),".2f"))
