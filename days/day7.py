import os

def num_bags_contain_bag(d, my_bag):
    res = rec(d, my_bag, {my_bag})
    print(len(res)-1)


def rec(d, cur_bag, bags_in):
    if not cur_bag in d.keys():
        return bags_in
    res = set({})
    for bag in d[cur_bag]:
        bags_in.add(bag)
        res = res.union(rec(d, bag, bags_in))
    return res


def rec2(d, cur_bag):
    res = 1

    for bag, c_bags in d[cur_bag].items():
        res += c_bags * rec2(d, bag)
    
    return res


def num_bag_bag_contain(d, my_bag):
    res = rec2(d, my_bag)
    print(res-1)


def parse_bags_contained(file_name):
    d = {}
    with open(file_name, 'r') as f:
        # parse bags and the bags they contain
        for line in f:
            line_splitted = line.split(' ')
            bag_s_idx = [i for i, elem in enumerate(line_splitted) if 'bag' in elem]
            big_bag = line_splitted[0] + line_splitted[1]
            for i in bag_s_idx[1:]:
                cur_bag = line_splitted[i-2]+line_splitted[i-1]
                if cur_bag == 'noother':
                    continue
                if cur_bag in d.keys():
                    d[cur_bag].append(big_bag)
                else:
                    d[cur_bag] = [big_bag]
    return d


def parse_bags_contain(file_name):
    d = {}
    with open(file_name, 'r') as f:
        for line in f:
            line_splitted = line.split(' ')
            bag_s_idx = [i for i, elem in enumerate(line_splitted) if 'bag' in elem]
            big_bag = line_splitted[0] + line_splitted[1]
            d[big_bag] = {}
            for i in bag_s_idx[1:]:
                cur_bag = line_splitted[i-2]+line_splitted[i-1]
                if cur_bag == 'noother':
                    continue
                d[big_bag][cur_bag] = int(line_splitted[i-3])
    return d


if __name__ == "__main__":
    file_name = os.path.join('inputs','day7.txt')

    print('part 1:')
    d = parse_bags_contained(file_name)
    my_bag = 'shinygold'
    num_bags_contain_bag(d, my_bag)
    
    print('part 2:')
    d = parse_bags_contain(file_name)
    num_bag_bag_contain(d, my_bag)


