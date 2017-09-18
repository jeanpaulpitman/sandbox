from user import User


def main():
    user1 = User("Bob")
    user2 = User("Jane")

    print(user1)
    print(user2)

    user1.give_taco(user2)
    print(user1)
    print(user2)

    user2.give_taco(user1)
    print(user1)
    print(user2)


main()
