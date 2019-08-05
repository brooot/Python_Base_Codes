
l=[1,3,5,7]
it=iter(l)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
