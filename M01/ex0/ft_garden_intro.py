def ft_garden_intro(name: str, height: str, age: str) -> None:
    print('Plant:', name)
    print('Height:', height)
    print('Age:', age)
    print('')


if __name__ == "__main__":
    print('=== Welcome to My Garden ===')
    ft_garden_intro("Rose", "25cm", "30 days")
    print('=== End of Program ===')