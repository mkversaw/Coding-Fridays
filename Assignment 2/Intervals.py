import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
	sorted_tuples = tuples_list
	sorted_tuples.sort()
	tuple_stack = []
	tuple_stack.append(sorted_tuples[0])
	for i in range(1,len(sorted_tuples)):
		if(tuple_stack[-1][1] < sorted_tuples[i][0]):
			tuple_stack.append(sorted_tuples[i])
		elif(tuple_stack[-1][1] < sorted_tuples[i][1]):
			lwr = tuple_stack[-1][0]
			upr = sorted_tuples[i][1]
			tuple_stack.pop()
			tuple_stack.append((lwr,upr))
	return tuple_stack
# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
	pass


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
	assert merge_tuples([(1,2)]) == [(1,2)]
	# write your own test cases
	
	assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
	# write your own test cases
	
	pass

def main():
	
	tuple_list = []
	lines = sys.stdin.readlines()
	intervals = int(lines.pop(0).strip()) # determine the number of intervals
	
	for i in lines:
		str = i.split()
		lower_bound = int(str[0])
		upper_bound = int(str[1])
		
		temp_tuple = (lower_bound,upper_bound)
		tuple_list.append(temp_tuple)
		
	new_list = merge_tuples(tuple_list)
	new_list.sort()
	for i in new_list:
		print(i)

if __name__ == "__main__":
	main()
