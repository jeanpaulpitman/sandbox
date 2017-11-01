
from random import randint


def get_random_numbers(number):
    unique_numbers = set()
    while len(unique_numbers) < number:
        random_number = randint(1, (number * 10))
        unique_numbers.add(random_number)
    random_numbers = list(unique_numbers)
    random_numbers.sort(reverse=True)
    return random_numbers


number_list = get_random_numbers(50)
print(number_list)