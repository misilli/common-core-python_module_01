#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = 0.0
        self._day = 0
        self.set_height(height)
        self.set_age(day)

    def grow(self, rate: float) -> None:
        self.set_height(self.get_height() + rate)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._day

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(height, 2)

    def set_age(self, day: int) -> None:
        if day < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._day = day

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._day} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str) -> None:
        super().__init__(name, height, day)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 day: int, trunk_diameter: float) -> None:
        super().__init__(name, height, day)
        self.trunk_dia = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_dia}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of", end=" ")
        print(f"{self.get_height()}cm long and {self.trunk_dia}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 day: int, harvest_season: str) -> None:
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, rate: float = 2.1) -> None:
        super().grow(rate)
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value:g}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
