import os


def check_validity1(password_line):
    borders, character, password = password_line.split(' ')
    count_c_occurance = password.count(character[0])
    down_boarder, up_boarder = borders.split('-')
    if count_c_occurance >= int(down_boarder) and count_c_occurance <= int(up_boarder):
        return True
    return False


def check_validity2(password_line):
    indices, character, password = password_line.split(' ')
    character = character[0]
    index1, index2 = indices.split('-')
    if ((password[int(index1)-1] == character and password[int(index2)-1] != character) or 
        (password[int(index2)-1] == character and password[int(index1)-1] != character)):
        return True
    return False


def process_passwords(passwords, check_validity_func):
    count_valid = 0
    for password in passwords:
        count_valid += check_validity_func(password)
    print(f'The number of valid passwords: {count_valid}')


if __name__ == "__main__":
    file_name = os.path.join('inputs', 'day2.txt')

    with open(file_name, 'r') as f:
        passwords = [x for x in f.readlines()]
    
    print('part1:')
    process_passwords(passwords, check_validity1)

    print('part2:')
    process_passwords(passwords, check_validity2)
