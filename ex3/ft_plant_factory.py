#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = round(height, 2)
        self.day = day

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)

    def age(self) -> None:
        self.day += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.day} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    print("Created:", end=" ")
    rose.show()
    oak = Plant("Oak", 200, 365)
    print("Created:", end=" ")
    oak.show()
    cactus = Plant("Cactus", 5, 90)
    print("Created:", end=" ")
    cactus.show()
    sunflower = Plant("Sunflower", 80, 45)
    print("Created:", end=" ")
    sunflower.show()
    fern = Plant("Fern", 15, 120)
    print("Created:", end=" ")
    fern.show()


if __name__ == "__main__":
    ft_plant_factory()
