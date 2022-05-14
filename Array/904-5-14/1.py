from typing import List

def totalFruit( fruits: List[int]) -> int:
    l, len_set, total = 0,1,0
    for r in range(1,len(fruits)):
        print(f'------r is {r}')
        if fruits[r] in fruits[l:r] and len_set < 2:
            total +=1
            len_set +=1
            print(f'total is {total}')
        elif fruits[r] in fruits[l:r] and len_set > 2 :
            total +=1
        elif  len(set(fruits[l:r])) >2:
            l +=1
    return total

totalFruit(fruits=[1,2,1])

#lst = [1,2,3,1]
#print(True if 5 in lst else False)
#print( len(set(lst)))