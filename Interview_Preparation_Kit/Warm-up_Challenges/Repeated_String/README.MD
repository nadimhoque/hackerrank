# Repeated Strings

My understanding of the problem is that the string s is repeated infinte times. We are to count the number of times the letter 'a' appears in the first 'n' characters.

The function has two inputs 's' which is the substring, and 'n' is the number of repeats.

## __Method 1__

EDIT: This was not the best method because this will fail if new repeated array is very large. 

1. Create a temp array. This array we will use the input array and repeat it n number of times. 
2. Make another loop that goes through the first n number of characters and count the number of 'a'

## __Method 2__
#
I attempted the array method but it will only work when the repeated array is small and fails when that array is large.

Since we know that we need to look at the first n number of characters, we might not even need create a temporary array with the string repeated n number of times. I think that the best route is to do the following:

1. Determine if the substring is only 'a'. If this is true then return 'n'
2. If the substring contains other characters then check if the modulo of 'n' and the length of 's' is zero. If it is zero then the number of 'a' is simply the number of 'a' in the substring multiplied by 'n' divided by the length of the string.
3. If the modulo of 'n' and the length of the string 's' is not zero then I did the following:
	- Set the intial total  number of 'a' be the number of 'a' in the substring multipied by the floor of 'n' and the length of 's'. I am doing the floor because there will be no remainder and if we muliply this number by the length of 's', then we are less then n.
	- To calculate the number of 'a' in the remainder we simply count the number of 'a' from the start of the substring to the modulo result from 's' and the length of the string 's'. We then add this number to the total of 'a' and return it.

## __Other Methods__

Though my solution works for the test cases I am pretty certain that I did not write it optimally. I will figure this out later when I am done with more challenges.
