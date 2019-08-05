
# class Car:
#     def run(self,speed):
#         print('速度%s'%speed)


# class ShipCar(Car):
#     def ship(self,km):
#         print('运送%s'%km) 

# s=ShipCar()
# s.run(100)
# s.ship('石油')
class Bycycle:
    def run(self,km):
        print('自行车里程:',km)


class EBycycle(Bycycle):
    def __init__(self,volume):
        self.volume=volume
    def run(self,km):
        e_km=min(km,self.volume*10) 
        self.volume-=e_km/10
        if e_km>0:
            print('电动骑行了%s公里，剩余电量%s'%(e_km,self.volume))
        if km>e_km:
            super().run(km-e_km)

e=EBycycle(10)
e.run(100)
e.run(150)

