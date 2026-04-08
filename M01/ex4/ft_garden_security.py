class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.i_age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.i_age} days old"

    def create_plant(self) -> str:
        return self.show()

    def set_height(self, h: int) -> None:
        if h > 0:
            self.height = h
            print('Height updated:', str(self.height) + 'cm')
        else:
            print(self.name, ": Error, height can't be negative")
            print("height update rejected")

    def set_age(self, a: int) -> None:
        if a > 0:
            self.i_age = a
            print('Age updated:', str(self.i_age), 'days')
        else:
            print(self.name, ": Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self.i_age

    def get_height(self) -> float:
        return self.height


if __name__ == "__main__":
    Plants = [
        Plant("Rose", 45, 30),
        Plant("Rose", 25, 30),
    ]
    print('=== Garden Security System ===')
    print('Plant created:', Plants[0].create_plant()+'\n')
    Plants[0].set_height(250)
    Plants[0].set_age(10)
    print()
    Plants[0].set_height(-50)
    Plants[0].set_age(-10)
    print()
    print('Current state:', Plants[0].show())
