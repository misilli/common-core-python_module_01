#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)

    def age(self) -> None:
        self.day += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    initial_height = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - initial_height, 2)}cm")


if __name__ == "__main__":
    ft_plant_growth()
