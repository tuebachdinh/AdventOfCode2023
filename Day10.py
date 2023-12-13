file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input10.txt'

with open(file_path, 'r') as file:
    count = 0 
    lines = file.readlines()
    x = 0
    y = 0
    check_x = 0 
    check_y = 0
    result = 0 

    def next(x,y,arr,check_x, check_y):
            path = 0
            x_new = 0
            y_new = 0
            if arr[x][y] == 'S' and count == 0:  
                path = arr[x][y-1]
                x_new = x
                y_new = y-1
            elif arr[x][y] == '-':
                if check_x == x and check_y == y+1:
                    path = arr[x][y-1]
                    x_new = x
                    y_new = y-1
                else:
                    path = arr[x][y+1]
                    x_new = x
                    y_new = y+1
            elif arr[x][y] == '|':
                if check_x == x+1 and check_y == y:
                    path = arr[x-1][y]
                    x_new = x-1
                    y_new = y
                else: 
                    path = arr[x+1][y]
                    x_new = x+1
                    y_new = y
            elif arr[x][y] == 'L':
                if check_x == x-1 and check_y == y:
                    path = arr[x][y+1]
                    x_new = x
                    y_new = y+1
                else:
                    path = arr[x-1][y]
                    x_new = x-1
                    y_new = y
            elif arr[x][y] == 'J':
                if check_x == x-1 and check_y == y:
                    path = arr[x][y-1]
                    x_new = x
                    y_new = y-1
                else:
                    path = arr[x-1][y]
                    x_new = x-1
                    y_new = y
            elif arr[x][y] == '7':
                if check_x == x+1 and check_y == y:
                    path = arr[x][y-1]
                    x_new = x
                    y_new = y-1
                else:
                    path = arr[x+1][y]
                    x_new = x+1
                    y_new = y
            elif arr[x][y] == 'F':
                if check_x == x+1 and check_y == y:
                    path = arr[x][y+1]
                    x_new = x
                    y_new = y+1
                else:
                    path = arr[x+1][y]
                    x_new = x+1
                    y_new = y
            check_x = x 
            check_y = y
            return path, check_x,check_y, x_new, y_new
   
    for index, line in enumerate(lines):
        for char in line:
            if char == 'S':
                y = line.index(char)
                x = index
    
    while result != 'S':
        result,check_x,check_y,x,y = next(x,y,lines,check_x,check_y)
        count += 1
    print(count//2)
    
    
        
    
    