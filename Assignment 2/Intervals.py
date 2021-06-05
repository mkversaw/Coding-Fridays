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
def sort_by_interval_size (tuples_list): #  bubble sort for intervals
	sorted_tuples = tuples_list
	for i in range(len(sorted_tuples)-1):
		for j in range(0,len(sorted_tuples)-(i+1)):
			weight1 = abs(sorted_tuples[j][1] - sorted_tuples[j][0])
			weight2 = abs(sorted_tuples[j+1][1] - sorted_tuples[j+1][0])
			if(weight1 > weight2):
				sorted_tuples[j],sorted_tuples[j+1] = sorted_tuples[j+1],sorted_tuples[j]
			elif(weight1 == weight2):
				if(sorted_tuples[j][0] > sorted_tuples[j+1][0]):
					sorted_tuples[j],sorted_tuples[j+1] = sorted_tuples[j+1],sorted_tuples[j]
	return(sorted_tuples)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
	try:
		assert merge_tuples([(1,2)]) == [(1,2)]
		assert merge_tuples([(14,17),(-8,-5),(26,29),(-20,-15),(12,15),(2,3),(-10,-7),(25,30),(2,4),(-21,-16),(13,18),(22,27),(-6,-3),(3,6),(-25,-14)]) == [(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]
		
		assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
		assert sort_by_interval_size([(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]) == [(2, 6), (12, 18), (-10, -3), (22, 30), (-25, -14)]
		
	except AssertionError as e:
		print("Test case(s) failed: ", e)
	else:
		print("Test cases passed!")

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
			
		merged_list = merge_tuples(tuple_list)
		print(merged_list)
		
		sorted_list = sort_by_interval_size(merged_list)
		print(sorted_list)
		
		test_cases()
	
	except FileNotFoundError:
		print("Failed to open file, did not exist")
	except Exception as e:
		print("Program failed: ", e)
	else:
		print("Program finished successfully")

if __name__ == "__main__":
	main()
