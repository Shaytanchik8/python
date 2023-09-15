def IsOddNumber(N):
    if N >= 0 and (N % 1 == 0):
        return True
    else:
        return False

k = float(input("N = "))
print(IsOddNumber(k))