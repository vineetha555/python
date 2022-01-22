class Vehicle:
    color='white'
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

    def get_result(self):
         return('vehicle name:',self.name,'speed:',self.speed,'mileage:',self.mileage)


class Bus(Vehicle):
    pass

schoolvolvo=Bus('schoolvolvo',100,12)
print(schoolvolvo.get_result())




# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18