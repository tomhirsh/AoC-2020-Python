import os

def check_ids_delta(ids):
    for i in range(len(ids)):
        if ids[i] - ids[i-1] == 2:
            return ids[i]-1


def process_line(line):
    line_bool = []
    for letter in line:
        if letter == 'R' or letter == 'B':
            line_bool.append(1)
        else:
            line_bool.append(0)
    return line_bool


def process_pass_single(pass1, low=0, high=127):
    # binary search - recursion
    if len(pass1) == 1:
        if pass1[0]:
            return high
        else:
            return low
    
    elif pass1[0]: #up/right
        return process_pass_single(pass1[1:],(high-low+1)//2 + low, high)
    else: #down/left
        return process_pass_single(pass1[1:],low, (high-low)//2 + low)


def part1(passes):
    max_id = -1
    for pass1 in passes:
        row = process_pass_single(pass1[:-3])
        col = process_pass_single(pass1[-3:], low=0, high=7)
        new_max = row * 8 + col
        if new_max > max_id:
            max_id = new_max
    return max_id

def part2(passes):
    ids = []
    for pass1 in passes:
        row = process_pass_single(pass1[:-3])
        col = process_pass_single(pass1[-3:], low=0, high=7)
        new_max = row * 8 + col
        ids.append(new_max)
    
    my_id = check_ids_delta(sorted(ids))
    return my_id


if __name__ == "__main__":
    file_name = os.path.join('inputs', 'day5.txt')
    passes = []
    with open(file_name, 'r') as f:
        for line in f:
            passes.append(process_line(line[:-1]))

    print('part1:')
    print(part1(passes))
    print('part2:')
    print(part2(passes))
