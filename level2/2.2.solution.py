path = []
record = [0] * 64

step_x = [-2,-2,-1,-1,1,1,2,2]
step_y = [-1,1,-2,2,-2,2,-1,1]

def solution(src, dst):
    record[src] = 1
    path.append(src)
    bpf(1)
    if record[dst] > 0:
        return record[dst] -1
    else :
        return 0

def bpf(path_len):
    path_next = 0
    while path_len > 0:
        path_len -= 1
        loc = path[0]
        path.pop(0)

        for i in range(0, len(step_x)):
            x = loc%8
            y = loc//8

            x += step_x[i]
            y += step_y[i]
            new_l = x + 8*y
            if x >=0 and x < 8 and y >=0 and y < 8 and record[new_l] == 0:
                path.append(new_l)
                path_next += 1
                record[new_l] = record[loc] + 1

    if path_next > 0:
        bpf(path_next)
                 
#solution(0, 5)
#print(record)