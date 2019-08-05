
def myyield():
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

a=iter(myyield())

print(next(a))
print(next(a))

