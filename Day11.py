import math
file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input11.txt'
with open(file_path, 'r') as file:
    count = 0 
    lines = file.readlines()
    table_horizontal = []
    table_vertical = []
    table = []
    xy_list = []
    ans = 0 
    scale = 2
    for line in lines:
        if '.'*(len(line)-1) == line.strip('\n'):
            for i in range(scale):
                table_horizontal.append(line.strip('\n'))

        else:
            table_horizontal.append(line.strip('\n'))
    
    for x in range(len(table_horizontal[0])): 
        line = ''
        for y in range(len(table_horizontal)):
            line += (table_horizontal[y][x])
        table_vertical.append(line)
    
    for line in table_vertical:
        if '.'*(len(line)) == line:
            for i in range(scale):
                table.append(line)
        else:
            table.append(line)
    
    for index,line in enumerate(table):
        x = index
        for char in line:
            if char == '#':
                y = line.index('#')
                xy_list.append((x,y))
                line = line.replace(line[y],'.',1)

    for (x,y) in xy_list:
        for (x1,y1) in xy_list:
            ans += abs(x1 - x) + abs(y1 - y)
            print
    
    print(ans//2)
    print(ans//2 + (10012422 - ans//2)*(1000000-scale))
    
    
    
