#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = 0.0
        self._day = 0
        self.set_height(height)
        self.set_age(day)

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.8)

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
            return
        self._height = round(height, 2)

    def set_age(self, day: int) -> None:
        if day < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._day = day

    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    print(f"Height updated: {rose.get_height():g}cm")
    print(f"Age updated: {rose.get_age()} days")
    rose.set_height(-67.0)
    rose.set_age(-67)
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
