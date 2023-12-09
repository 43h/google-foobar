#Input:
#solution.solution('1211', 10)
#Output:
#    1

#Input:
#solution.solution('210022', 3)
#Output:
#    3


def reverse(n):
    l = len(n)
    x = ''
    for i in range(l -1 , -1, -1):
        x = x  + n[i]
    return x
   

def descending_order(n):
    ls=list(n)
    ls.sort()
    return ''.join(ls)

def subtraction(x, y, base):
    l = len(x)
    flag = 0
    rst = ''
    for i in range(l-1, -1, -1):
        a = int(x[i]) - int('0')
        b = int(y[i]) - int('0')
        if flag == 1 :
            if a > 0:
                a -= 1    
                flag = 0
            else:
                a = base -1

        if a >= b :
            rst = rst + str(a-b)
        else :
            flag = 1
            rst = rst + str(base + a - b)

    return rst


def solution(n, b):
    t_dict = {}
    l = []
    l_num = 0
    while 1:
        y = descending_order(n)
        x = reverse(y)
        n = reverse(subtraction(x, y, b))
    
        if int(n) == 0:
            return 1
        else :
            if n in t_dict:
                t_dict[n] += 1
                if l.count(n) == 0:
                    l.append(n)
                else:
                    break
            else :
                t_dict[n] = 1
    return len(l)

print(solution('1211', 10))