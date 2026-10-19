#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self):
        self.height = round(self.height + 0.8, 2)

    def age(self):
        self.day += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.day} days old")


def ft_plant_growth() -> None:
    rose = Plant("rose", 25, 30)
    print("=== Garden Plant Registry ===")
    i = 1
    while i <= 7:
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
        i += 1


if __name__ == "__main__":
    ft_plant_growth()
