__author__ = 'HP'


def fizz_buzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    # For very large numbers calculate the cross sum first and then check if the cross sum is a multiple of 3
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

