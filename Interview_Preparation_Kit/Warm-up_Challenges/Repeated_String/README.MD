# Repeated Strings

My understanding of the problem is that the string s is repeated infinte times. We are to count the number of times the letter 'a' appears in the first n characters.

## __Method 1__

I think that the best method for this is using arrays. Assuming the above description is accurate then 

1. Create a temp array. This array we will use the input array and repeat it n number of times. 
2. Make another loop that goes through the first n number of characters and count the number of 'a'

## __Method 2__
#
I attempted the array method but it will only work when the repeated array is small and fails when that array is large.

Since we know that we need to look at the first n number of characters, we might not even need create a temporary array with the string repeated n number of times. I think that the best route is to do the following:

1. Count the number of 'a' in the substring
2. Check if the modulo of the temp string and the number of repeats is zero. If it is then we can assume that we can multiply the number of 'a' in the substring by the number of repeats
3. If the modulo from step 2 is not zero then we count the number of 'a' is the remainder. With that we can multiply the number of 'a' in the substring by the repeats - 1 and add the number of 'a' that appears in the remainder substring.
