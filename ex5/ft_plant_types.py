#!/usr/bin/env python3






class Plant:



        self.set_height(height)

r, height: int, day: int) -> None:



        self.name = name
        self.set_he

ight(height)


    def age(self):




    def get_height(self):


        self.set_height(se

    def get_age(self):





        self.set_age(self.day + 1)



    def get_height(sel

f):



        return self.height
        else:


    def get_age(self):



        return self.day








    def set_height(self, height: float) 
        else:


        if height < 0:



            print(f

"{self.name}: Error, height can't be negative")



            print("H

eight update rejected")
        else:





            self.height = 

round(height, 2)

    


    def set_age(self, day:

 int) -> None:



        if day < 0:





            print(f"{self.name}: Error, age can't be negat
        else:


            print("Age update rejected")


        else:



            self.day = day






    def show(self):dia




        print(f"{self.name}: Height = {self.height}cm, Age = {self.day} days")



class Flower(Plant):





    def __init__ (self,  name: str, height: int, day: int, color: str) -> none:

        Plant.__init__(self, name, height, day)

        self.color = color

        self._bloomed = False
    

    def show(self)-> None:

        Plant.show()

        print(f" Color: {self.color}")

        if self._bloomed:

            print(f"{self.name} is blooming beautifully!")
        else:

            print(f"{self.name} has not blomed yet")


    def bloom(self) -> None:

        self._bloomed = True


class Tree(Plant):

    def __init__(self, name: str, height: int, day: int, trunk_dia: float) -> None:

        Plant.__init__(self, name, height, day)
        self.trunk_dia = trunk_dia


    def show(self) -> None:
        Plant.show()
        print(f" Trunk diameter: {self.trunk_dia}cm")
    
    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of", end=" ")
        print(f"{self.get_height()}cm long and {self.trunk_dia}cm wide.")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, day: int, harvest_time: str) -> None:
        Plant.__init__(self, name, height, day)
        self.harvest_time = harvest_time
        self.nutritional = 0.0

     def grow(self, rate: float = 1.0) -> None:
        Plant.grow(rate)
        self.nutritional += 0.5
