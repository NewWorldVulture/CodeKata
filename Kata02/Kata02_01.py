# Kata02: Karate Chop
# By Ada

# Goal: Implement a binary search routine
# Method 01: Tail Recursion approach

def chop(target_int, source_list, index_count=0):
	# If we run out of list to search, return -1
	# This signifies that the integer is not in the list
	if source_list == []:
		return -1
	
	# Get half the list length ...
	# ... unless the list is empty. In which case, return 1
	half_len = max(len(source_list)//2, 1)
	
	# Handle cases for if target int is equal, greater...
	# ... than, or less than the median value of the list
	if target_int == source_list[half_len - 1]:
		return index_count + half_len - 1
	
	# If the number we're checking against is too small, cut the list, take the lower half 
	elif target_int < source_list[half_len - 1]:
		# take [:half_len - 1], otherwise it takes too much and throws off the index
		return chop(target_int, source_list[:half_len - 1], index_count)
	
	# ... Otherwise, take the upper half of the list.
	elif target_int > source_list[half_len - 1]:
		return chop(target_int, source_list[half_len:], index_count + half_len)
