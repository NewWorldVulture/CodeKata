# Kata02: Karate Chop
# By Ada

# Goal: Implement a binary search routine
# Method 02: while looping w/pointer

def chop(target_i, source_list):
    # Initialize upper and lower bounds, initialize range 
    upper =  len(source_list)
    lower = 0
    
    # Skip if we're dealing with empty set
    # If we're checking a range of 0, the target doesn't exist
    while lower != upper:
        pointer = (lower + upper)//2
        
        # We found him, boys.
        if source_list[pointer] == target_i:
            # print(str(pointer))
            return pointer
        
        # If the pointer is too big, lower the upper bound
        elif source_list[pointer] > target_i:
            upper = pointer
        # Else, raise the lower bound!
        else:
            lower = pointer + 1

    # If the target doesn't exist, return -1
    return -1


