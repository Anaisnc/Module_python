class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.i_age = age

    def show(self) -> str:

        return f"{self.name.capitalize()}: {round(self.height, 1)}cm, {self.i_age} days old"


    def set_height(self, h: int) -> None:
        if h > 0:
            self.height = h
        else:
            print("height update rejected")

    def set_age(self, a: int) -> None:
        if a > 0:
            self.i_age = a
        else:
            print("Age update rejected")

    def get_age(self) -> int:
        return self.i_age

    def get_height(self) -> float:
        return self.height

    def age(self) -> int:
        self.i_age += 1
        return self.i_age

    def grow(self) -> float:
        self.height += 2.1
        return self.height



    @staticmethod
    def check_age(age: int) -> None:
        res = age > 365
        print(f"Is {age} more than a year? ->{res}")

    class Stats:
        def __init__(self, grow_count: int, age_count: int, show_count: int) -> None:
            self.grow_count = grow_count
            self.age_count = age_count
            self.show_count = show_count

        def show_stat(self) -> None:
            print(f"Stats: {self.grow_count} grows,{self.age_count} age, {self.show} shows")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str, is_bloom: bool) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = is_bloom

    def bloom(self) -> None:
        self.is_bloom = True
        print(self.name.capitalize(), 'is blooming beautifully!')

    def show(self) -> None:
        print('=== Flower')
        print(super().show())
        print("Color:", self.color)
        status = 'blooming' if self.is_bloom else 'not bloomed yet'
        print(f'{self.name} has {status}')
        s = f"[statistics for {self.name}]"
        print(s.capitalize())
        print("Color:", self.color)
        self.bloom()

class Tree(Plant):
    def __init__(self,name: str, height: float, age: int, trunk_diameter: float, shade: bool) -> None:
        super().__init__(name, height, age)
        self.diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self) -> None:
        self.shade = True
        print("Tree", self.name, "now produces a shade of",self.height , "cm long and",self.diameter , "cm wid")

    def show(self) -> None:
        print('\n=== Tree')
        print(super().show())
        print('Trunk diameter:', self.diameter, 'cm')
        s = f"[asking the {self.name} to produce shade]"
        print(s.capitalize())
        self.produce_shade()

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int, days: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.days = days

    def produce_nutritional_value(self) -> None:
        for _ in range(self.days):
            self.nutritional_value += 1
        print('Nutritional value:', self.nutritional_value)

    def grow(self) -> None:
        for _ in range(self.days):
            super().grow()

    def age(self) -> None:
        for _ in range(self.days):
            super().age()

    def show(self) -> None:
        print('\n=== Vegetable')
        print(super().show())
        print('Harvest season:', self.harvest_season)
        print('Nutritional value:', self.nutritional_value)
        s = f"[[make {self.name} grow and age for {self.days} days]]"
        print(s.capitalize())
        self.grow()
        self.age()
        print(super().show())
        print('Harvest season:', self.harvest_season)
        self.produce_nutritional_value()

if __name__ == '__main__':
    plants = [
        Plant("Rose", 15.0, 10),
        Plant("Oak", 200.0, 365),
        Plant("Tomato", 5.0, 10),
    ]
    print('=== Garden Plant Types ===')
    f = Flower(plants[0].name, plants[0].height, plants[0].i_age, 'red', False)
    t = Tree(plants[1].name, plants[1].height, plants[1].i_age, 5.0, False)
    v = Vegetable(plants[2].name, plants[2].height, plants[2].i_age, 'April', 0, 20)
    f.show()
    t.show()
    v.show()
