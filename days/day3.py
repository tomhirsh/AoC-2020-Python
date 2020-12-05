import os
import numpy as np

def trees_process(line):
    return [1 if c=='#' else 0 for c in line]


def read_map(file_name):
    tree_map = []
    with open(file_name, 'r') as f:
        lines = [x for x in f.readlines()]
    
    for line in lines:
        tree_map.append(trees_process(line[:-1]))
    
    return np.array(tree_map)


def count_trees(delta_i=1, delta_j=3):
    tree_counter = 0
    i = delta_i
    j = delta_j % tree_map.shape[1]
    while i < tree_map.shape[0]:
        if tree_map[i][j] == 1:
            tree_counter += 1
        i += delta_i
        j = (j+delta_j) % tree_map.shape[1]
    return tree_counter


if __name__ == "__main__":
    tree_map = read_map(os.path.join('inputs','day3.txt'))
    print('part1:')
    print(count_trees())

    print('part2:')
    given_slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)] # (down=i, right=j)
    mul_res = 1
    for i,j in given_slopes:
        mul_res *= count_trees(i, j)
    print(f'result: {mul_res}')