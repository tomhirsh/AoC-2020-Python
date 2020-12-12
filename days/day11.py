import os
import numpy as np
from collections import Counter

# idx = (np.abs(np.where(np.diag(seats, 1) == -1)[0] - 1)).argmin()


def change_seats(seats, min_occupied=4):
    changed = False
    new_seats = -1 * np.ones(shape=seats.shape)
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            count_occupied = 0
            cur_place = seats[i][j]
            if cur_place == d['.']:
                new_seats[i][j] = d['.']
                continue
            kernel = seats[max(i-1, 0): min(i+2, seats.shape[0]), 
                            max(j-1, 0): min(j+2, seats.shape[1]) ]
            count_occupied = np.count_nonzero(kernel == 1)
            
                
            if count_occupied == 0:
                new_seats[i][j] = d['#']
                changed = True
            elif cur_place == d['#'] and count_occupied > min_occupied:
                new_seats[i][j] = d['L']
                changed = True
            else:
                new_seats[i][j] = cur_place

    return new_seats, changed


def part1(seats):
    changed = True
    while changed:
        seats, changed = change_seats(seats)
    return np.count_nonzero(seats == 1)


if __name__ == "__main__":
    file_path = os.path.join('inputs', 'day11.txt')
    global d 
    d = {'.': -1, 'L':0, '#':1}
    seats = []
    with open(file_path, 'r') as f:
        for line in f:
            seats.append([d[x] for x in line[:-1]])
    seats = np.array(seats)
    print('part1:')
    print(part1(seats))
