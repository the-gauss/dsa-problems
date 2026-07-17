"""Tower of Hanoi."""


def move_disk(from_pole, to_pole):
    print(f"Move disk from {from_pole} to {to_pole}")


def hanoi(n, from_pole, to_pole, with_pole):
    if n == 1:
        move_disk(from_pole, to_pole)
    else:
        hanoi(n - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        hanoi(n - 1, with_pole, to_pole, from_pole)


if __name__ == "__main__":
    hanoi(3, "A", "C", "B")
