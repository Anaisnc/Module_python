class   Plant:

    def __init__(self, name: str, height: str, age: str) -> None:
        self.name = name
        self.height = height
        self.i_age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.i_age} days old"

if __name__ == "__main__":
    Plant1 = Plant("Rose", "25cm", "30 days old")
    Plant2 = Plant("Sunflower", "80cm", "45 days old")
    Plant3 = Plant("Cactus", "15cm", "120 days old")

    print('=== Garden Plant Registry ===')
    print(Plant1.show())
    print(Plant2.show())
    print(Plant3.show())