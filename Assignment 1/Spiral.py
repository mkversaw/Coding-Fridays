import sys

def main():   
    # open file w/ name spiral.in
    try:
       
        #file = open(fileName) # open file then read lines
        lines = sys.stdin.readlines()
        spiral = []
        
        for line in lines:
            str_line = line.rstrip() # strip any new lines
            int_line = int(str_line) # insert elements as INTEGERS
            spiral.append(int_line)
        
        size = spiral[0]
        
        
        spiral2D = create_spiral(size)
        
        
        print_2D(spiral2D,size)
        print(sum_adjacent_numbers(spiral2D, 1))
    
    except FileNotFoundError:
        print("Failed to open file, did not exist")
    except Exception as e:
        print("Program failed: ", e)
    else:
        print("Program finished successfully")


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):
    if(n < 1):
        raise ValueError("Given spiral size is invalid (less than 1)")
    elif(n > 99):
        raise ValueError("Given spiral size is invalid (more than 99)")
    elif( (n % 2) == 0 ):
        n += 1
    
    list2D = [[]]
    
    counter = 1
    move = 1
    x = int(n/2) 
    y = int(n/2) 
    
    
    rows, cols = (n, n)
    arr = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        arr.append(col)
    list2D = arr
    
    
    # Y THEN X  !!!!!!!
    list2D[x][y] = 1
    
    #print_2D(list2D,n)
    
    
    while(counter < n**2):

        for right in range(move):
            counter += 1
            if(counter <= n**2):
                x += 1
                list2D[y][x] = counter
                #print_2D(list2D,n)
            
        for down in range(move):
            
            counter += 1
            if(counter < n**2):
                y += 1
                list2D[y][x] = counter
                #print_2D(list2D,n)
            
        move += 1
        
        for left in range(move):
            
            counter += 1
            if(counter < n**2):
                x -= 1
                list2D[y][x] = counter
                #print_2D(list2D,n)
            
        for up in range(move):
            
            counter += 1
            if(counter < n**2):
                y -= 1
                list2D[y][x] = counter
                #print_2D(list2D,n)
        
        move += 1
    #print_2D(list2D,n)
    return list2D
    
    

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    sum = 0
    length = len(spiral)
    for i in range(length):
        for j in range(length):
            if(n == spiral[i][j]):
                try:
                    sum += spiral[i-1][j+1]
                except:
                    sum += 0
                try:
                    sum += spiral[i][j+1]
                except:
                    sum += 0
                try:
                    sum += spiral[i+1][j+1]
                except:
                    sum += 0
                    
                try:
                    sum += spiral[i-1][j]
                except:
                    sum += 0
               
                try:
                    sum += spiral[i+1][j]
                except:
                    sum += 0
               
                try:
                    sum += spiral[i-1][j-1]
                except:
                    sum += 0
                    
                try:
                    sum += spiral[i][j-1]
                except:
                    sum += 0
                    
                try:
                    sum += spiral[i+1][j-1]
                except:
                    sum += 0
               
               
    return sum
                
    
    
    

def print_list (list):
    for i in list:
        print(i)

def print_2D (list, size):
    for i in range(size):
        for j in range(size):
            print(str(list[i][j]).ljust(4," "), end = " ")
        print()
    print()

if __name__ == "__main__":
    main()
