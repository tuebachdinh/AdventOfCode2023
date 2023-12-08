import math
file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input8.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    map = {}
    for index in range(2,740):
        map[lines[index][0]+lines[index][1]+lines[index][2]] = [lines[index][7]+lines[index][8]+lines[index][9], lines[index][12]+lines[index][13]+lines[index][14]]
    A_map = {}
    A_list = [number for number in list(map.keys()) if number[-1]== 'A']
    A_check = [number for number in list(map.keys()) if number[-1]== 'A']
    
    for index, start in enumerate(A_list):    
        count = 0 
        for direction in (lines[0].replace('\n',''))*1000000:  
            if start[-1] == 'Z' :
                A_map[A_check[index]] = count
                break
            else:
                if direction == 'L':
                    start = map[start][0]
                    count += 1
                elif direction == 'R':
                    start = map[start][1]
                    count += 1

    print(math.lcm(*list(A_map.values())))
    