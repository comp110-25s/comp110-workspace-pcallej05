"""Planning a cozy tea party!"""

__author__: str = "730658315"


def main_planner(guests: int) -> None:
    """The entrypoint of this program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """The number of tea bags required"""
    return people * 2


def treats(people: int) -> int:
    """The number of treats required"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of tea party materials"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
