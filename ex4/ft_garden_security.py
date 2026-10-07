#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(day)

    def grow(self):
        self.set_height(self.height + 0.8)

    def age(self):
        self.set_age(self.day + 1)

    def get_height(self):
        return self.height

    def get_age(self):
        return self.day

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = round(height, 2)

    def set_age(self, day: int) -> None:
        if day < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.day = day

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.day} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: " , end="")
    rose.show()
    print()

    rose.set_height(25.0)
    rose.set_age(30)
    print(f"Height updated: {rose.get_height()}cm")
    print(f"Age updated: {rose.get_age()} days\n")
    rose.set_height(-67.0)
    rose.set_age(-67)
    print()
    print("Current state: ", end="")
    rose.show()

if __name__ == "__main__":
    ft_garden_security()
