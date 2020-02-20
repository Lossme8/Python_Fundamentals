import game


def main():
    min = 1
    max = 6

    def rollDice():
        numberofRolls = int(input("How many times would you like to roll the dice? "))
        count = numberofRolls
        while numberofRolls >= count and count > 0:
            print(random.randint(min, max))
        count = count - 1

    rollDice()


main()
