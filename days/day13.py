import os
import numpy as np

def part1(num, busses):
    find_time = lambda x: ((num // x + 1) * x , x)
    times = find_time(busses)
    ideal_time_idx = np.argmin(times[0])
    ideal_time, ideal_idx = times[0][ideal_time_idx], times[1][ideal_time_idx]
    return (ideal_time - num) * ideal_idx


def part2(busses):
    prod = 1
    for d in busses.T[0]:
        prod *= d

    tot = 0
    for bus in busses:
        inverse = pow(int(prod // bus[0]), -1, int(bus[0])) # python 3.8+
        tot += -bus[1] * (prod // bus[0]) * inverse

    return tot % prod
    

if __name__ == "__main__":
    file_name = os.path.join('inputs', 'day13.txt')
    with open(file_name, 'r') as f:
        num = int(f.readline()[:-1])
        busses = np.array([int(x) for x in f.readline()[:-1].split(',') if x!= 'x'])
    print(part1(num, busses))

    with open(file_name, 'r') as f:
        num = int(f.readline()[:-1])
        busses = np.array([[int(x),i] for i, x in enumerate(f.readline()[:-1].split(',')) if x!= 'x'])
    print(part2(busses))