class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.i_age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.i_age} days old"

    def create_plant(self) -> str:
        return self.show()


if __name__ == "__main__":
    Plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    print('=== Plant Factory Output ===')
    for Plant in Plants:
        print('Created:', Plant.create_plant())
