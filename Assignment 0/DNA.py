import sys
import fileinput

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
def longest_subsequence (s1, s2):	
	# ensures that s1 is the longer of the two strings (unless they're equal)
	if(len(s1) > len(s2)):
		s1 = s1.upper()
		s2 = s2.upper()
	else:
		s3 = s1.upper()
		s1 = s2.upper()
		s2 = s3
	
	any_check = False
	current_longest = [""]
	
	for i in range(len(s2)):
		for j in range(i,len(s2)):
			temp_str = s2[i:j] # from root index to current j index
			if(temp_str in s1 and len(temp_str) > 1): # don't care if the sequence is 1 long
				if(len(temp_str) > len(current_longest[0])):
					current_longest.clear() # clear the list, we have a new KING
					current_longest.append(temp_str)
				elif(len(temp_str) == len(current_longest[0])):
					current_longest.append(temp_str) # if it equals the largest, then append
				any_check = True
	current_longest.sort()
	if(any_check):			
		return current_longest
	else:
		return []
		# no common subsequences found

def main():
	
	try:
		lines = sys.stdin.readlines()
		sequence_length = int(lines.pop(0).strip()) # get the length of the sequence
		for i in range(sequence_length):
			s1 = lines.pop(0)
			s2 = lines.pop(0)
			seq = longest_subsequence(s1,s2)
			if(len(seq) == 0):
				print("No common subsequences found")
			else:
				for j in seq:
					print(j)
			print()
	
	except FileNotFoundError:
		print("Failed to open file, did not exist")
	except Exception as e:
		print("Program failed: ", e)
	else:
		print("Program finished successfully")

if __name__ == "__main__":
	main()
