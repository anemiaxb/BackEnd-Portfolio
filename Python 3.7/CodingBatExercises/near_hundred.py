# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)


print(near_hundred(91))
