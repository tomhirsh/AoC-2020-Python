import os

def find_inf_loop(progs, i=0):
    if i == len(progs):
        return 0, False
    if progs[i]['c'] > 0:
        return 0, True
    
    acc_val = progs[i]['d']
    progs[i]['c'] += 1
    if progs[i]['op'] == 'nop':
        return find_inf_loop(progs, i+1)
    elif progs[i]['op'] == 'acc':
        res = find_inf_loop(progs, i+1)
        return res[0] + acc_val, res[1]
    else: # jmp
        return find_inf_loop(progs, i+acc_val)


def get_acc_before_inf_loop(ops):
    num = find_inf_loop(ops)
    print(num)


def process_lines(file_path):
    progs = []
    with open(file_path, 'r') as f:
        for line in f:
            op, num = line[:-1].split(' ')
            progs.append({'op':op, 'd':int(num), 'c':0})
    return progs


if __name__ == "__main__":
    file_path = os.path.join('inputs','day8.txt')
    ops = process_lines(file_path)
    print('part1:')
    get_acc_before_inf_loop(ops)
    print('part2:')
    for i, op1 in enumerate(ops):
        if op1 == 'acc':
            continue
        
        new_ops = [{'op': x['op'], 'd':x['d'], 'c':0} for x in ops]
        if op1['op'] == 'jmp':
            new_ops[i]['op'] = 'nop'
        elif op1['op'] == 'nop':
            new_ops[i]['op'] = 'jmp'
        acc, inf_loop = find_inf_loop(new_ops)
        if not inf_loop:
            print(acc)
            break