file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input5.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    seeds1 = lines[0].strip('seeds: ').strip('\n').split(' ')
    seeds2 = []
    for i in range(0, len(seeds1)-1,2):
        seeds2 += [num for num in range(int(seeds1[i]),int(seeds1[i])+int(seeds1[i+1]))]
    
    map = {}
    def convert(number, range):
        for index in range:
            check = lines[index].strip('\n').split(' ')
            if int(check[1]) <= number <= int(check[1]) + int(check[2]) - 1:
                return int(check[0]) + number - int(check[1])
        return number
    ans = 10000000000000000 
    for number in seeds2:
        soil = convert(int(number), range(3,13))
        fert = convert(soil, range(15,64))
        water = convert(fert, range(66,108))
        light = convert(water, range(110,159))
        temp =  convert(light, range(161,187))
        humid = convert(temp, range(189,228))
        location = convert(humid, range(230,239))
        if location < ans:
            ans = location
    print(ans)