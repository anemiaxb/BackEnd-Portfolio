# Given an int num, return the absolute difference between n and 32, except return triple the absolute difference if n is over 32.
def diff32(num):
    if num < 32:
        return 32 - num
    else:
        return 3 * (num - 32)


print(diff32(22))
print(diff32(34))
