import os
from functools import lru_cache


@lru_cache(None)
def rec_arrange(i, cur_jolt):
    if cur_jolt == adapters[-1]:
        return 1
    elif i == len(adapters):
        return 0
    
    adapter = adapters[i]
    diff = adapter - cur_jolt

    if diff <= 3:
        return rec_arrange(i+1, cur_jolt) + rec_arrange(i+1, adapter)
    
    return 0


def count_arrangements():
    counter = rec_arrange(0, 0)
    return counter


# straight forward implementation
def count_differences():
    cur_jolt = 0
    jolts_diffs = {}
    jolts_diffs[3] = 1
    for i, adapt in enumerate(adapters):
        diff = adapt - cur_jolt

        if diff <= 3:
            if diff in jolts_diffs.keys():
                jolts_diffs[diff] += 1
            else:
                jolts_diffs[diff] = 1
        
        else:
            cur_jolt = adapters[i-1]
            diff = adapt - cur_jolt
            if diff in jolts_diffs.keys():
                jolts_diffs[diff] += 1
            else:
                jolts_diffs[diff] = 1
        cur_jolt = adapters[i]

    return jolts_diffs[3] * jolts_diffs[1]


if __name__ == "__main__":
    file_path = os.path.join('inputs', 'day10.txt')
    global adapters
    adapters = []
    with open(file_path, 'r') as f:
        for line in f:
            adapters.append(int(line[:-1]))
    adapters.sort()

    print('part 1:')
    print(count_differences())
    print('part 2:')
    print(count_arrangements())