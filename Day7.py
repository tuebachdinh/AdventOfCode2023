file_path = '/Users/tueeee/Documents/Advent Of Code 2023/Input/input7.txt'
with open(file_path, 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    criteria = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    map = {}
    ans1 = 0 
    five_kind = []
    four_kind = []
    full_house = []
    three_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    
    for line in lines: 
        map[line.split(' ')[0]] = line.split(' ')[1].replace('\n','')
  
    for card in list(map.keys()):
        A_, K_, Q_, J_, T_, r9, r8, r7, r6, r5, r4, r3, r2 = 0,0,0,0,0,0,0,0,0,0,0,0,0
        for number in card:
            if number == 'A':
                A_ += 1
            elif number == 'K':
                K_ += 1
            elif number == 'Q':
                Q_ += 1
            elif number == 'J':
                J_ += 1 
            elif number == 'T':
                T_ += 1
            elif number == '9':
                r9 += 1
            elif number == '8':
                r8 += 1
            elif number == '7':
                r7 += 1
            elif number == '6':
                r6 += 1
            elif number == '5':
                r5 += 1
            elif number == '4':
                r4 += 1
            elif number == '3':
                r3 += 1
            elif number == '2':
                r2 += 1
        check_list = [A_, K_, Q_, J_, T_, r9, r8, r7, r6, r5, r4, r3, r2]
        check_list1 = [r for r in check_list if r != 0]

        #for part 2 and change the criteria
        """for r in check_list1:
            if J_ == r:
                check_list1.remove(J_)
                check_list1.append(0)
                break
        check_list1[check_list1.index(max(check_list1))] += J_"""
        
        check_list = check_list1

        if 5 in check_list:
            five_kind.append(card)
        elif 4 in check_list:
            four_kind.append(card)
        elif 3 in check_list and 2 in check_list:
            full_house.append(card)
        elif 3 in check_list and 1 in check_list:
            three_kind.append(card)
        elif check_list.count(2) == 2:
            two_pair.append(card)
        elif check_list.count(1) == 3:
            one_pair.append(card)
        else:
            high_card.append(card)
    
    def choose_better(old,new):
        for index in range(len(old)):
            if criteria[old[index]] > criteria[new[index]]:
                return old
            elif criteria[old[index]] < criteria[new[index]]:
                return new
            else:
                pass
    
    def order(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if choose_better(arr[j], arr[j+1]) == arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    final = order(high_card) + order(one_pair) + order(two_pair) + order(three_kind) + order(full_house) + order(four_kind) + order(five_kind)
    
    for index,card in enumerate(final,1):
        ans1 += int(map[card])*index
   
    print(ans1)
   


    
    


  

