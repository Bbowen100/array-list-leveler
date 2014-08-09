Summary
==================

So a pre-school teacher gathered her little ones for recess and needed to make 5 teams from the five classes that she had. However each class had a different number of students so she had to move some children to other classes so that the numbers would be even and fair games could be played. 

This program essentially takes a list of lists and moves the elements around until the arrays are as equal in number as they can be.

Algorithm
=========
mean = average amount of elements in the set of a arrays

excess = length(largest_array) - mean

floaters = number of elements % number of arrays

1. take the sum of the number of elements in each array
2. integer-divide the sum by the number of arrasy to find the mean
3. Loop (while the excess is greter than the floaters on the top)
{ go through each array
   find the smallest in the list and the largest
   calculate the excess in the larger and move the 
   excess amount to the smallest }
