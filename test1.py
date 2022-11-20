# import time as new_time_name
# from random import random, randint as custom_randint
#
#
# print(f"{random()=}")
# print(f"{custom_randint(0, 100)=}")
# print(f"{new_time_name.time()=}")
#
# import math
#
# x = math.factorial(1200)
# print(x)

import requests

# def get_name():
#     print(f"{__name__=} inside function")
# if __name__ == '__main__':
#     get_name()

from name_of_your_module import get_name

if __name__ == '__main__':
    get_name()
    print(f"I'm your Father, bcs my {__name__=}")