import logging
from random import randint
from log_setup import setup

logging.basicConfig(filename='logs.log', format='{asctime} {levelname} {funcName}->{lineno}: {msg}', style='{', encoding='utf-8', level=setup)

def factorial(num):
    if not isinstance(num, int):
        raise ValueError
    elif num <= 0:
        logging.error(f"Degree {num} must be more than zero")
        raise ValueError("Degree must be more than zero")
    fact = ''
    for i in range(num, 0, -1):
        factor = randint(1, 101)
        if factor == 0:
            continue
        elif factor == 1:
            factor = ''
        else:
            factor = f'{factor}*x^{i} + ' if i != 1 else f'{factor}*x + '
        fact += factor 
    fact += f'{randint(1, 101)} = 0'
    return fact


if __name__ == "__main__":
    try:
        k = int(input('Enter natural degree k: '))
        res = factorial(k)
        logging.info(f'Factor with degree {k} is {res}')
    except Exception as ex: 
        logging.exception(f'Degree must be natural number. Exception: {ex}')
