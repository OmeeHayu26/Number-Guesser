import random


def generate_number(num1: int, num2: int) -> int:
    if num1 < num2:
        return random.randint(num1, num2)
    else:
        return random.randint(num2, num1)


def scan_number() -> int:
    i = 0
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Please enter an integer" + i * '!')
            i += 1


def main() -> None:
    num1 = scan_number()
    num2 = scan_number()
    guess = generate_number(num1, num2)
    num_user = scan_number()
    answer = num_user == guess
    print(f"You guessed: {num_user}. {answer}, the number was: {guess}")


if __name__ == '__main__':
    main()

