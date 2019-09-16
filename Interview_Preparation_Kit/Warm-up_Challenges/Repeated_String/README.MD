# Repeated Strings

My understanding of the problem is that the string s is repeated infinte times. We are to count the number of times the letter 'a' appears in the first n characters.

## __Method__

I think that the best method for this is using arrays. Assuming the above description is accurate then 

1. Create a temp array. This array we will use the input array and repeat it n number of times. 
2. Make another loop that goes through the first n number of characters and count the number of a's

## __Alternatives__

Since we know that we need to look at the first n number of characters, we might not even need create a temporary array with the string repeated n number of times. 
