class Car(object):

    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("Price:",self.price)
        print("Speed:",self.speed)
        print("Fuel:",self.fuel)
        print("Mileage:",self.mileage)

        if(self.price>10000):
            self.tax=0.15

        print("Tax:",self.tax)
        print("\n")

lightning_mcqueen = Car(2000,"35mph","Full","15mpg")
doc_hudson = Car(2000,"5mph","Not Full","105mpg")
mack = Car(2000,"15mph","Kind of Full","95mpg")
mater = Car(2000,"25mph","Full","25mpg")
luigi = Car(2000,"45mph","Empty","25mpg")
lizzie = Car (2000000,"35mph","Empty","15mpg")
