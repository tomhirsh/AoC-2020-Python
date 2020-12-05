import os

def part1(numbers, num):
    for i, num_i in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            if num_i + numbers[j] == num:
                mul_res = num_i * numbers[j]
                print(f'i = {num_i}, j = {numbers[j]}, mul_res = {mul_res}')

def part2(numbers, num):
    for i, num_i in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if num_i + numbers[j] + numbers[k] == num:
                    mul_res = num_i * numbers[j] * numbers[k]
                    print(f'i = {num_i}, j = {numbers[j]}, k={numbers[k]}, mul_res = {mul_res}')


if __name__ == "__main__":
    file_name = os.path.join('inputs', 'day1.txt')
    num = 2020

    with open(file_name, 'r') as f:
        numbers = [int(x) for x in f.readlines()]
    
    print('part1:')
    part1(numbers, num)

    print('part2:')
    part2(numbers, num)


