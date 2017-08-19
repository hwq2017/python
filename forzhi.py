# flag = 1
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0:
#             flag = 0
#             break
#         else:
#             flag = 1
#     if flag == 1:
#         print i


for i in range(1,1000):
    n = 0
    for j in range(1,i):
        if i % j == 0:
            n = n + j
    if n == i:
        print n
