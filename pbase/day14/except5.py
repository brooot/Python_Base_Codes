def a():
    try :
        d=int(input('shuru:'))
    except ValueError:
        d=1
    div =10/d
    print(div)
def b():
    a()
def c():
    b()
c()