def solution(x, y):
    rst = 0    
    m = int(x)
    f = int(y)

    while m!=f and m > 0 and f > 0:
        if m > f:
            # 如果差异太大，多减些
            if m > 10*f:
                multi = (int(m/f) -1)
                rst += multi
                m = m - (multi*f)
            else:
                m = m -f
                rst += 1
        else:
            if f > 10*m:
                multi = (int(f/m) -1)
                rst += multi
                f = f - (multi*m)
            else:
                f = f -m
                rst += 1

    if m == 1 and f == 1:
        return str(rst)

    return 'impossible'

#print(solution('4', '7'))