
#(0-1): 0 ^ 1 = 1 (1)
#(0-2): 0 ^ 1 ^ 2 = 3 (2+1)
#(0-3): 0 ^ 1 ^ 2 ^ 3 = 0 (0)
#(0-4): 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4 (4)

#(0-5): 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1 (1)
#(0-6): 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 = 7 (6+1)
#(0-7): 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^  7 = 0 (0)
#(0-8): 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8 (8)

#So the pattern for finding the xor between all the integers between 0 to n is:
#if n%4 == 1 then, answer = 1
#if n%4 == 2 then, answer = n+1
#if n%4 == 3 then, answer = 0
#if n%4 == 0 then answer = n 

def cal(x):
    result = [x, 1, x+1, 0]
    return result[x % 4]

def solution(start, length):
    res=0

    for i in range(0, length):
        s = start + i * length -1
        e = start + i * length + length - i - 1
        print(s," ",e)
        res ^= cal(s) ^ cal(e)
    return res

print(solution(0, 3))