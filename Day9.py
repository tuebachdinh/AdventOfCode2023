file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input9.txt'

with open(file_path, 'r') as file:
    
    lines = file.readlines()
    
    def convert(arr): 
        result = []
        for i in range(len(arr)-1):
            result.append(arr[i+1] - arr[i])
        return(result)
    def all_zeros(arr):
        for number in arr:
            if number != 0:
                return False
        return True

    ans1 = 0
    ans2 = 0
    
    for line in lines:
        new_line = [int(number) for number in line.strip('\n').split(' ')]
    
        check_list = new_line
        next_number = new_line[-1]
        pre_number = new_line[0]
        check_plus_or_mimus = 0
        
        while not all_zeros(check_list):
            check_list = convert(check_list)
            next_number += check_list[-1]
            if check_plus_or_mimus%2==0:
                pre_number -= check_list[0]
            else:
                pre_number += check_list[0]
            
            check_plus_or_mimus+=1
        
        ans1 += next_number
        ans2 += pre_number
            
        
    print(ans1)
    print(ans2)

