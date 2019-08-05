class dog:
    pass
dog1=dog()
dog2=dog()
dog1.kinds='京巴'
dog1.id='京0001'
dog1.color='白色'
dog2.kinds='到盲'
dog2.color='黑色'
def show_info(d):
    print('种类：',d.kinds,'颜色',d.color)
show_info(dog1)
show_info(dog2)