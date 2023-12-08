file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input6.txt'

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    times = [number for number in lines[0].replace('\n','').split(' ') if number.isdigit()]
    distances = [number for number in lines[1].replace('\n','').split(' ') if number.isdigit()]
    actual_time = ''
    actual_distance = ''
    
    ans1 = 1
    ans2 = 0
    for index,time in enumerate(times):
        actual_time += time
        actual_distance += distances[index]
        result = []
        for x in range(0,int(time)):
            if x*(int(time)-x) >= int(distances[index]):
                result.append(x)
        ans1 *= (max(result)-min(result) + 1)
    for x in range(0, int(actual_time)):
        if x*(int(actual_time)-x) >= int(actual_distance):
            ans2 = int(actual_time) - 2*x + 1
            break



    print(ans1)
    print(ans2)
        

