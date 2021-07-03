# 100％
def solution(N):
    # write your code in Python 3.6
    bin = format(N, 'b')
    max_val = 0
    tmp = 0
    for i in bin:
        if i == '1':
            start_flag = True
            val = tmp
            max_val = max(max_val, val)
            tmp = 0
        elif start_flag:
            tmp += 1
    return max_val
