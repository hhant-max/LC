def judgeSquareSum(c: int) -> bool:
    # first find the biggest that square that bigger than 
    if c ==0: return True
    l,r = 0, c
    while l < r:
        mid = (l+r)//2
        if mid * mid > c:
            r = mid
        else:
            l = mid +1
            res = l

    a = res-1  # res is index
    print(a)
    # in this list find the combination
    for i in range(0,a+1):
        for j in range(i,a+1):
            # how to desingn if I gind anyone not everyone
                if (i)**2 + (j)**2 == c:
                    return True

    return False
