# 66％
def solution(A):
    # write your code in Python 3.6
    max_A = max(A)
    if max_A < 0:
        return 1
    else:
        for i in range(1, max_A + 1):
            if i not in A:
                ans = i
                break
            else:
                ans = i + 1
        return ans
