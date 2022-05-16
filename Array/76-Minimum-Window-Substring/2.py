def minWindow(s: str, t: str) -> str:
    countT, window = {},{}

    # transfer t into a dict---- key:string value : count number: dictionary get function.
    # 没用数个数的函数二十手动便利每一个， 并且如果存在的话就加到字典并且再原来的基础上加。 如果不存在就返回0
    for i in t:
        countT[i] = 1 + countT.get(i,0)

    countT_number, window_number = len(countT), 0

    res, reslen = [-1,-1], float("infinity")


    l = 0
    for r in range(len(s)):
        c = s[r]

        if c in countT.keys():
            window[c] = 1 + window.get(c,0)
            
            # 注意这边的问题是 window【c】不存在怎么办
            if window[c] == countT[c]:
                window_number += 1

            while window_number == countT_number:
                # update the result
                if (r-l + 1) < reslen:
                    res = [l,r]
                    reslen = r-l + 1

                # left pop
                if s[l] in countT.keys():
                    #window[s[l]] = -1 + window.get(r)
                    window[s[l]] -= 1
                #print(f"s[l] is {s[l]}")
                #print(f"count_number is {countT_number[s[l]]}")
                    if window[s[l]] < countT[s[l]]:
                        window_number -= 1

                l += 1

    l, r = res
    return s[l:r+1]
        

s = "ADOBECODEBANC"
t = "ABC"
minWindow(s=s, t=t)

#print(len(s))
#print(s[1])