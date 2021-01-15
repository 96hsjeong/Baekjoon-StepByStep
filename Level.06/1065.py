def function(n):
    ls = [int(i) for i in str(n)]
    if len(ls) <= 2:
        return True
    else:
        for i in range(1, len(ls)):
            difference = ls[i] - ls[i - 1]
            if i != 1 and difference != temp:
                return False
            temp = difference
    return True

n = int(input())
ls = [i for i in range(1, n+1) if function(i)]
print(len(ls))