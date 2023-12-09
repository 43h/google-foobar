def solution(data, n):
    t_dict = {}
    rst = []
    for x in data:
        if x in t_dict:
            t_dict[x] += 1
        else :
            t_dict[x] = 1

    for x in data:
        if t_dict[x] <= n:
            rst.append(x)
    return rst


print(solution([1,2,1,5,3,4], 1))