"""
  Class implementing the factorial function
"""


def factorial(number:int)->int:
    if number < 0:
        raise Exception("The value must non negative")
    elif number == 0 or number == 1:
        result:int = 1
    else:
        result = number * factorial(number - 1)

    return result


class Factorial(object):
    def __init__(self):
        pass

    def compute(self, number:int):
        return factorial(number)
