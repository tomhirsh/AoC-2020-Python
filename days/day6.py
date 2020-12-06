import os

def part1(file_name):
    c =0 
    li = []
    with open(file_name, 'r') as f:
        for line in f:
            if line == '\n':
                li = []
                continue
            
            for l in line[:-1]:
                if not l in li:
                    li.append(l)
                    c += 1    
    return c


def part2(file_name):
    c = 0
    d = {}
    count_all = 0
    with open(file_name, 'r') as f:
        for line in f:
            if line == '\n':
                count_all += sum([1 for v in d.values() if v==c])
                d = {}
                c = 0
                continue

            for l in line[:-1]:
                if l in d:
                    d[l] += 1
                else:
                    d[l] = 1
            c += 1
    # last group
    count_all += sum([1 for v in d.values() if v==c])
    
    return count_all

if __name__ == "__main__":
    file_name = os.path.join('inputs', 'day6.txt')
    print('part1:')
    print(part1(file_name))
    print('part2:')
    print(part2(file_name))
