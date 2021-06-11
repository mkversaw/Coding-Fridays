import sys
import math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
	n = (int(math.ceil(math.sqrt(len(strng)))))
	table_len = n**2
	pads = table_len - len(strng)
	message = []
	
	for i in strng:
		message.append(i)
	
	for i in range(pads):
		message.append('*')
	
	message[::-1]
	
	message2 = []
	
	k = 0
	k2 = n
	
	#print(n)
	
	for i in range (0,n):
		temp = message[k:k2]
		
		message2.append(temp)
		k += n
		k2 += n
		
	message2 = message2[::-1]
	
	message3 = ""
	
	for j in range(0,n):
		for i in message2:
			if(i[0] != '*'):
				message3 += i[0]
			i.pop(0)
		
	#print(message3)
	
	return message3
	
	
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
	n = (int(math.ceil(math.sqrt(len(strng)))))
	table_len = n**2
	pads = table_len - len(strng)
	message = []
	
	for i in strng:
		message.append(i)
	
	
	for i in range(pads):
		message.append('*')
		
	message2 = []
	
	print
	print(message)
	print
	
	k = 0
	k2 = n
	
	#print(n)
	
	for i in range (0,n):
		temp = message[k:k2]
		message2.append(temp[::-1])
		k += n
		k2 += n
	#
	
	print(message2)
	
	pass

def main():
	# read the strings P and Q from standard input
	lines = sys.stdin.readlines()
	p_string = lines[0].strip()
	q_string = lines[1].strip()
	
	#print(p_string)
	
	bingus = encrypt(p_string)
	print(bingus)
	
	floppa = decrypt(bingus)
	print(floppa)
	
	# encrypt the string P
	
	# decrypt the string Q
	
	# print the encrypted string of P
	# and the decrypted string of Q

if __name__ == "__main__":
	main()


