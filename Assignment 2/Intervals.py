import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
	list_length = len(tuples_list)
	merged_tuples = []
	for i in range(list_length):
		lwr = tuples_list[i][0] # lower bound
		upr = tuples_list[i][1] # upper bound
		for j in range(i,list_length):
			lwr2 = tuples_list[j][0]
			upr2 = tuples_list[j][1]
			if(lwr >= lwr2 and lwr < upr2):
				lwr = lwr2
				tuples_list.pop(j)
				list_length -= 1
			if(upr <= upr2 and upr > lwr2):
				upr = upr2
				tuples_list.pop(j)
				list_length -= 1
			#print(tuples_list)
		#merged_tuples.append((lwr,upr))
	return merged_tuples

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
	
	try:
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
	
	except FileNotFoundError:
		print("Failed to open file, did not exist")
	except Exception as e:
		print("Program failed: ", e)
	else:
		print("Program finished successfully")

if __name__ == "__main__":
	main()
