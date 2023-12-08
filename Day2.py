
import re

file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input2.txt'
# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    ans1 = 0 
    ans2 = 0 
    for index, line in enumerate(lines, 1):
        blue = []
        green = [] 
        red = []
        new_line = line.strip('Game ' + str(index)).strip(": ")
        line_list = new_line.split(';')
        for turn in line_list:
            turn_list = turn.split(',')
            for number in turn_list:
                if "red" in number:
                    red += [int(output) for output in re.findall(r'\d+', number)]
                if "green" in number:
                    green += [int(output) for output in re.findall(r'\d+', number)]
                if "blue" in number:
                    blue += [int(output) for output in re.findall(r'\d+', number)]
        if max(red) <= 12 and max(green) <= 13 and max(blue) <= 14:
            ans1 += index
        ans2 += max(red)*max(blue)*max(green)
    print(ans1)
    print(ans2)
        
        
        
        


