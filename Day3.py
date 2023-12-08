import re
file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input3.txt'
with open(file_path, 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    ans1 = 0 
    set = []
    set.append("."*(len(lines[1])+1))
    for line in lines: 
        new_line = line.replace("\n","")
        set.append("."+new_line+".")
    set.append("."*(len(lines[10])+1))
    sum0 = []
    minus = []
    for index, line in enumerate(set):
    
        if index != 0 and index != 141:
            number_list = re.findall(r'\d+', line)
            sum0 += number_list
            
            for number in number_list:
                index_number = line.find(number)
                
                check = []
                
                for i in range (index_number - 1,index_number + len(number) + 1):
                    if (line[i] == "." or line[i].isdigit()) and (set[index-1][i] == ".") and (set[index+1][i] == "."):
                        check.append(1)
                if sum(check) == (len(number) +2):
                    minus.append(number) 
                #line = line.replace(number, "."*len(number))
                

    for x in sum0:
        ans1 += int(x)
   
    for y in minus:
        ans1 -= int(y)
 
    #print(sum0)
    #print(minus)
    print(ans1)



   
   
   
 