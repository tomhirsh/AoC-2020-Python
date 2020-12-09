import os

def is_sum_of_prev_d(num, check_list):
    for i, num1 in enumerate(check_list):
        for num2 in check_list[i+1:]:
            if num1 + num2 == num:
                return True
    return False


def part1(numbers_list, d=5):
    for i, num in enumerate(numbers_list[d:]):
        if not is_sum_of_prev_d(num, numbers_list[i:i+d]):
            return num

def contiguous_set_numbers(invalid_num, check_list, set_len):
    for i, num in enumerate(check_list[set_len:]):
        sum_set = sum(check_list[i:i+set_len])
        if sum_set == invalid_num:
            return max(check_list[i:i+set_len]), min(check_list[i:i+set_len])
    return None

if __name__ == "__main__":

    file_name = 'day9.txt'
    file_path = os.path.join('inputs',file_name)
    with open(file_path, 'r') as f:
        numbers_list = [int(x[:-1]) for x in f]
    print('prat 1:')
    invalid_num = part1(numbers_list, d=25)
    print(invalid_num)

    print('part2:')
    set_len = 2
    minmax = contiguous_set_numbers(invalid_num, numbers_list, set_len)
    while not minmax:
        set_len += 1
        minmax = contiguous_set_numbers(invalid_num, numbers_list, set_len)
    
    print(minmax[0]+minmax[1])