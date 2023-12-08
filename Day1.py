
file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input.txt'

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    ans1 = 0 
    # Process each line
    for line in lines:
        for letter in line:
            if letter.isdigit():
                ans1 += int(letter)*10
                break
        for letter in line[::-1]:
            if letter.isdigit():
                ans1 += int(letter)
                break
    
    checked_number = ["one","1","two","2","three","3","four","4","five","5","six","6","seven","7","eight","8","nine","9"]
    map = {"one" : 1, "two": 2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9 }
    
    ans2 = 0 
    for line in lines: 
        number_of_line1 = 0
        number_of_line2 = 0 
        
        for index in range(len(line)):
            for check in checked_number:
                if line[index:].startswith(check):
                    if check.isdigit():
                        number_of_line1 += int(check)*10
                    else:
                        number_of_line1 += map[check]*10
                    break
            if number_of_line1 != 0:
                ans2 += number_of_line1
                break
        
        for index in range(len(line)):
            for check in [number[::-1] for number in checked_number]:
                if line[::-1][index:].startswith(check):
                    if check.isdigit():
                        number_of_line2 += int(check)
                    else:
                        number_of_line2 += map[check[::-1]]
                    break
            if number_of_line2 != 0:
                ans2 += number_of_line2
                break


    print(ans1)
    print(ans2)
