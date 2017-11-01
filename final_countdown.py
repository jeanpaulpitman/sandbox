def main():
    seconds_to_die = int(input(">>"))
    final_countdown(seconds_to_die)


def final_countdown(seconds_to_die):
    for i in reversed(range(seconds_to_die + 1)):
        print(i)


main()
