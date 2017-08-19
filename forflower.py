for i in range(100,1000):
    g = i % 10
    t = i % 100 / 10
    h = i / 100
    if i == g ** 3 + t ** 3 + h ** 3:
        print i
    else:
        pass
