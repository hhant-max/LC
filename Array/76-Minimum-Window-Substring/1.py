def  minwindow(s, t) -> str:
    countT, window = {},{}

    # transfer t into a dict---- key:string value : count number: dictionary get function.
    # 这边有问题!!!!!
    for s in t:
        countT[s] = 1 + countT.get(s,0)
    
    countT_number, window_number = len(countT), 0
    res, reslen = [-1,-1], float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]
        print(f'r is {r}, c is {c}')



    l, r = res
    return s[l:r+1]

s = "ADOBECODEBANC"
t = "ABC"
minwindow(s, t)

#print(len(s))
#print(s[1])