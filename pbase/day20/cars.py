
class Car:

    def run(self, speed):
        print('汽车以%s速度行驶' % speed)


class Plane:

    def fly(self, height: '高度'):
        print('飞机以%s高度飞行' % height)


class PlaneCar(Car, Plane):
    pass


p1 = PlaneCar()
p1.fly(10000)
p1.run(300)
