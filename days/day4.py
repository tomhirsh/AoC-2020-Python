import os

def process_pasports(file_path, part=1):
    counter_valid_passports = 0
    cur_passport = []
    comp_passport = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

    comp_passport_cid = sorted(['cid'] + comp_passport)
    
    with open(file_path, 'r') as f:
        for line in f:

            if line == '\n':
                if (sorted(cur_passport) == comp_passport_cid 
                    or sorted(cur_passport) == comp_passport):
                    
                    counter_valid_passports += 1
                cur_passport = []

            fields = line[:-1].split(':')

            for i, field in enumerate(fields):
                if field[-3:] in comp_passport_cid:
                    if part == 1:
                        cur_passport.append(field[-3:])
                    elif valid_field(field[-3:], fields[i+1].split(' ')[0]):
                        cur_passport.append(field[-3:])
        
        # last passport
        if sorted(cur_passport) == comp_passport_cid or sorted(cur_passport) == comp_passport:
            counter_valid_passports += 1

    return counter_valid_passports


def field_values_in_between(val, low, high):
    return int(val) >= low and int(val) <= high


def valid_field(field, val):
    # not efficient, but provids a correct answer
    if field == 'byr':
        return field_values_in_between(val, 1920, 2002)
    if field == 'iyr':
        return field_values_in_between(val, 2010, 2020)
    if field == 'eyr':
        return field_values_in_between(val, 2020, 2030)
    if field == 'hgt':
        if val[-2:] == 'cm':
            return field_values_in_between(val[:-2], 150, 193)
        elif val[-2:] == 'in':
            return field_values_in_between(val[:-2], 59, 76)
    if field == 'ecl':
        return (val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if field == 'pid':
        if len(val) == 9:
            for i in val:
                if ord(i) < 48 or ord(i) > 57:
                    return False
            return True
        return False
    if field == 'hcl':
        if val[0]=='#' and len(val)==7:
            for i in val[1:]:
                if (ord(i) <48 or (ord(i) > 57 and ord(i) <97) or ord(i) > 102):
                    return False
            return True
        return False
    if field == 'cid':
        return True


if __name__ == "__main__":
    print('part1:')
    print(process_pasports(os.path.join('inputs','day4.txt')))
    print('part2:')
    # also check the validity of the fields
    print(process_pasports(os.path.join('inputs','day4.txt'), part=2))