#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def grow(self) -> None:
            self._grow += 1

        def age(self) -> None:
            self._age += 1

        def show(self) -> None:
            self._show += 1

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

    def __init__(self, name: str, height: float, day: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._day: int = 0
        self.set_height(height)
        self.set_age(day)
        self._stats: Plant._Stats = Plant._Stats()

    def grow(self, rate: float) -> None:
        self._stats.grow()
        self.set_height(self.get_height() + rate)

    def age(self, days: int = 1) -> None:
        self._stats.age()
        self.set_age(self.get_age() + days)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._day

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> "Plant._Stats":
        return self._stats

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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.show()
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
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

    def __init__(
        self, name: str, height: float, day: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, day)
        self._tree_stats: Tree._TreeStats = Tree._TreeStats()
        self._stats = self._tree_stats
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._tree_stats.shade()
        print(f"Tree {self._name} now produces a shade of", end=" ")
        print(
            f"{self.get_height()}cm long and "
            f"{self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, day: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, rate: float = 2.1) -> None:
        super().grow(rate)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value:g}")


class Seed(Flower):
    def __init__(self, name: str, height: float, day: int, color: str) -> None:
        super().__init__(name, height, day, color)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()
