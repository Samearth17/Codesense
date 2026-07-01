#!/usr/bin/env python

def solve_equation(eqn):
    eqn_parts = eqn.split(' ')

    # co-efficients of x and y
    a = int(eqn_parts[0].replace('x', ''))
    b = int(eqn_parts[2].replace('y', ''))

    # RHS value
    c = int(eqn_parts[4])

    # solving the equation
    x = (c - (b * 3)) / (2 * a)
    y = (5 - (2 * x)) / 3

    return x, y


if __name__ == '__main__':
    eqn = '2x + 3y = 5'
    x, y = solve_equation(eqn)

    print(f'Equation: {eqn}\n')
    print(f'x = {x}')
    print(f'y = {y}')