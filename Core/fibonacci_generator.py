def fig():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

g = fig()
for i in range(9):
    print g.next(),