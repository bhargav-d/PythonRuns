# ***** Testing Lamba Functionality****
def sumOf(func, lb, ub):
    print("inside sumOf")
    sum = 0
    while (lb <= ub):
        sum = sum + func(lb)
        lb += 1
    return sum


print("in between")

res = sumOf(lambda i: i * i, 1, 3)
print(res)
