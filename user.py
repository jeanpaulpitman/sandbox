"""Module."""


class User:
    """Class."""
    INITIAL_SCORE = 0
    INITIAL_TACOS_TO_GIVE = 5

    def __init__(self, name=""):
        """Method."""
        self.name = name
        self.tacos_to_give = self.INITIAL_TACOS_TO_GIVE
        self.score = self.INITIAL_SCORE

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.tacos_to_give)

    def give_taco(self, user):
        self.tacos_to_give -= 1
        user.score += 1


if __name__ == '__main__':
    print("I'm in User!")
    u = User("Bob")
    print(u)
