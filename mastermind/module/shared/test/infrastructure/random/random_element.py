import random
from typing import Iterable

sys_random = random.SystemRandom()


def random_element(some_iterable: Iterable):
    return sys_random.choice(some_iterable)
