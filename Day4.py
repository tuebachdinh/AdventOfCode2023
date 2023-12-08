
file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input4.txt'

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    ans1 = 0 
    map = {}
    number_of_card = {}
    for index, line in enumerate(lines, 1):
        count = 0 
        new_pair = line.strip('Card').strip(' ').strip(str(index) + ':').strip('\n').split('|')
        result = [number for number in new_pair[0].split(' ') if number.isdigit()]
        check = [number for number in new_pair[1].split(' ') if number.isdigit()]
        for number in check:
            if number in result:
                count += 1
        
        map[index] = count
        number_of_card[index] = 1
        if count == 0:
            ans1 += count
        else:
            ans1 += pow(2, count - 1)
    
    for index in range(1, len(lines) + 1):
        for i in range(1, index):
            if map[i] + i >=  index:
                number_of_card[index] += number_of_card[i]


    ans2 = sum(list(number_of_card.values()))

    print(ans1)
    print(ans2)
    