def runnerup(arr):

    #this line sorts the arry in ascending order
    arr.sort()
    
    #since the list is sorted we can assume the term at the end is the largest. I used pop because it also removes the item from the list
    max = arr.pop(-1)
    #Setting up i so that it is the condition of the while loop
    i = 1
    #I am assuming we are also going to have a non empty list and not all of the elements are going to be the same.
    while i > 0:
        #temporarily set the temp variable to the item at the end of the list. For now we assume it is the second largest. If it equals the max then we start the loop over, but if not then we found the second and we set i to be lower then 0 so the loop ends
        temp = arr.pop(-1)
        if temp != max:
            sec=temp
            i = -10
           
    return sec

if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().split()))
    print(runnerup(arr))
