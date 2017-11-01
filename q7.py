
from random import randint


def get_random_numbers(number):
    random_numbers = set()
    while len(random_numbers) < number:
        random_number = randint(1, (number * 10) + 1)
        random_numbers.add(random_number)
    return list(random_numbers)


number_list = get_random_numbers(5)
print(number_list)