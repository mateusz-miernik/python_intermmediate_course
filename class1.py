"""
car_01 = {
    'carBrand': 'Seat',
    'carModel': 'Ibiza',
    'carIsAirBagOK': True,
    'carIsPaintingOK': True,
    'carIsMechanicOK': True
}

car_02 = {
    'carBrand': 'Opel',
    'carModel': 'Astra',
    'carIsAirBagOK': True,
    'carIsPaintingOK': False,
    'carIsMechanicOK': True
}


def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK']
                and aCar['carIsMechanicOK'])


print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = [car_01, car_02]
for c in cars:
    print('{} {} damaged = {}'.format(c['carBrand'], c['carModel'], IsCarDamaged(c)))
"""
# ---------------------------------------------
brandOnSale = 'Opel'


class Car:
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print("Air Bag - ok -       {}".format(self.isAirBagOK))
        print("Painting - ok -       {}".format(self.isPaintingOK))
        print("Mechanic - ok -       {}".format(self.isMechanicOK))
        print("IS ON SALE - ok -       {}".format(self.__isOnSale))
        print('------------------------\n')

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing SALE status for {} to {}'.format(self.brand, self.__isOnSale))
        else:
            print('Cannot change SALE status for {}. It is avaialble only for {}'.format(self.brand, brandOnSale))

    def __DelIsOnSale(self):
        del self.__isOnSale
    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, __DelIsOnSale, 'if set to true, the car is available in sale/promo')

    @classmethod
    def ReadTextFromLine(cls, text):
        aNewCar = cls(*text.split(':'))
        return aNewCar

    @staticmethod
    def KM_to_KW(KM):
        return KM*0.735

    @staticmethod
    def KW_to_KM(KW):
        return KW*1.36


print('Class level variables BEFORE creating instances:', Car.numberOfCars, Car.listOfCars)

car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Astra', True, True, False, True)

car_02.__isOnSale = False

car_01.GetInfo()
car_02.GetInfo()
print(vars(car_01))
print(vars(car_02))

print('Status of cars: {} {}'.format(car_01.IsOnSale, car_02.IsOnSale))
car_01.IsOnSale = True
car_02.IsOnSale = False
print('Status of cars after changing: {} {}'.format(car_01.IsOnSale, car_02.IsOnSale))


lineOfText = 'Renault:Megane:True:True:False:True'
car_03 = Car.ReadTextFromLine(lineOfText)
car_03.GetInfo()

"""
print('Class level variables AFTER creating instances:', Car.numberOfCars, Car.listOfCars)

car_01.GetInfo()
car_02.GetInfo()

print('Id of class is:', id(Car))
print('Id of instances are:', id(car_01), id(car_02))

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type:', type(car_01) is Car)
print('Check if object belongs to class using __class__:', car_01.__class__)

print("List of instance attributes with values:", vars(car_01))
print("List of class attributes with values:", vars(Car))

print("List of instance attributes with values:", dir(car_01))
print("List of class attributes with values:", dir(Car))

print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)
"""
