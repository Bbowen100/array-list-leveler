'''leveling arrays Algorithm

excess = len(big_array) - mean
floaters = number of elements % number of arrays

1. take the sum of the number of elements in each array
2. integer-divide the sum by the number of arrasy to find the mean
3. Loop (while the excess is greter than the floaters on the top)
{ go through each array
   find the smallest in the list and the largest
   calculate the excess in the larger and move the 
   excess amount to the smallest }

'''
import sys

def count(lst, num=0):
    '''(list)->int
    this function will take an array that is at the most 2 dimensional and will 
    count the amount of elements inside the given array.
    
    >>> count([[1,2],[5,9],[6,6,1]])
    7
    '''
    if(lst == []):
        #base case (it is finished!)
        return num
    
    elif(not(isinstance(lst[0],list))):
        # when the value is a str or int
        num+=1
        return count(lst[1:],num)
    
    elif(isinstance(lst[0],list)):
        #takes the len() of the nested list and adds it to the current sum
        num += len(lst[0])
        return count(lst[1:],num)
    
#DONE! COUNT() WILL RETURN THE NUMBER OF ELEMENTS IN A 2 DIMENSIOANL LIST/ARRAY


#BRACE YOURSELF! YOU HAVE ENTERED THE THIRD AND FINAL STEP

def big_small(lst):
    '''(list)-> tuple
    this function will find the largest list and the smallest list 
    and will then return a tuple with the index of the largest first and the 
    index of the smallest second
    
    >>> big_small([[1,2,3], [1,2], [2]])
    (0, 2)
    '''
    big = 0
    small = 0
    index = 0
    
    while (index < len(lst)):
        
        #which is the biggest!?
        if(len(lst[index]) > len(lst[big])):
            big = index
            
        #which is the smallest?!    
        if(len(lst[index]) < len(lst[small])):
            small = index
            
        #the counter must move    
        index+=1
        
    # gimme the answer    
    return (big, small)

#SO YOU FOUND THE BIGGEST AND THE SMALLEST        

#YOU DID IT CONGRATULATIONS...YAY!!!        
#TIME TO DO SOME TESTING...OK DONE!

# LEVELING ARRAYS MAIN

def main():
    '''(null) -> null
    '''
    # FIRST MESSAGE TO THE USER
    print()
    print('An Array should be of the form "[a,b,c,d,1,2,3]"')
    print('Please enter 0 arrays into the program to stop it')
    
    while(True):    

        num_arrays = int(input('   please enter the number ofarrays you wish to have: '))
        if(num_arrays > 0):
            array_lst = []
            i = 1
            while i <= num_arrays:
                curr_array = input('please enter array # '+str(i)+' : ')
                n_array = curr_array.strip('[').strip(']').split(',')
                array_lst.append(n_array)
                i+=1
            print(array_lst)
            
            # THE NESTED LIST OF ARRAYS HAS BEEN MADE (AND USER PROMPT)
            
            #FOR SOME REASON YOU TRIED TO MAKE A RECURSIVE FUNCTION THAT SUMMED NESTED LISTS
            #HERE idk WHY?
            
            bs_tuple = big_small(array_lst)
            mean = count(array_lst) // num_arrays
            excess = len(array_lst[bs_tuple[0]]) - mean
            floaters = count(array_lst) % num_arrays
            i = 0
            
            while (excess > floaters):
                while(i < excess):
                    array_lst[bs_tuple[1]].insert(0, array_lst[bs_tuple[0]].pop(0))
                    i+=1
                bs_tuple = big_small(array_lst)
                excess = len(array_lst[bs_tuple[0]]) - mean
            print(array_lst)
        
        elif(num_arrays == 0):
            sys.exit()
        
if(__name__ == '__main__'):
    main()
