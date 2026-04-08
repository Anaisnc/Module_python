class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.i_age = age

    def age(self) -> int:
        self.i_age += 1
        return self.i_age

    def grow(self) -> float:
        self.height += 0.8
        return self.height

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.i_age} days old"

    def get_info(self) -> None:
        h = self.grow()
        a = self.age()
        print(self.name + ':', str(round(h, 1)) + 'cm,', str(a), 'days old')

if __name__ == "__main__":
    time = 7
    i = 1
    Plants = [
        Plant("Rose", 25.0, 30),
        Plant("Rose", 25.0, 30),
    ]
    print('=== Garden Plant Growth ===')
    temp_h = Plants[0].height
    print(Plants[0].show())
    for _ in range(i, time + 1):
        print('=== Day', i, '===')
        Plants[0].get_info()
        i = i + 1
    t = Plants[0].height - temp_h
    print('Growth this week:', str(round(t, 1))+'cm')
