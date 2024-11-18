 

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

   #creating a display method
    def display_info(self):
        print(f'Car Make: {self.make}')
        print(f'Car Model: {self.model}')
        print(f'Car Year: {self.year}')

    #creating instance of the car
Car1 = Car("Camry Spider" ,"Toyota", 2019 )
Car1.display_info()