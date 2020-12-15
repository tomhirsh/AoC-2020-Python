import os

def process_mask(mask, part=1):
    mask_itself = mask.split(' ')[-1][:-1]
    if part == 1:
        return {len(mask_itself)-1-int(i):val for i,val in enumerate(mask_itself) if val!='X'}
    else:
        return {len(mask_itself)-1-int(i):val for i,val in enumerate(mask_itself)}

def process_masks(mask):
    masks = []
    mask_itself = mask.split(' ')[-1][:-1]
    mask2 = '0'*36
    mask_neutral = ''.join([x if x!='X' else '0' for x in mask_itself])
    masks.append(mask2)
    for i, x in enumerate(mask_itself):
        if x == 'X':
            new_masks = []
            for mask_i in masks:
                new_masks.append(mask_i)
                new_masks.append(mask_i[:i]+'1'+mask_i[i+1:])
            masks = new_masks
    return int(mask_neutral,2), [int(mask, 2) for mask in masks]

def part1(file_path):
    convert2bin = lambda x, n: format(x, 'b').zfill(n)
    memo = {}
    with open(file_path, 'r') as f:
        mask = f.readline()
        mask_proc = process_mask(mask)
        for line in f:
            if line[:4] == 'mask':
                mask_proc = process_mask(line)
                continue

            mem_val, num = line[:-1].split('=')
            mem_val = int(mem_val[4:-2])
            b_num = convert2bin(int(num[1:]), 36)[::-1]

            for i in range(len(b_num)):
                if i in mask_proc:
                    b_num = b_num[:i] + mask_proc[i] + b_num[i+1:]
            num = int(b_num[::-1], 2)
            memo[mem_val] = num
    return sum(list(memo.values()))
        

def part2(file_path):
    memo = {}
    with open(file_path, 'r') as f:
        mask = f.readline()
        mask_neutral, masks = process_masks(mask)
        
        for line in f:
            if line[:4] == 'mask':
                mask_neutral, masks = process_masks(line)
                continue

            mem_val, num = line[:-1].split('=')
            mem_val = int(mem_val[4:-2])
            num = int(num[1:])

            for m in masks:
                new_addr = (mem_val | mask_neutral) ^ m
                memo[new_addr] = num
            
    return sum(list(memo.values()))
    

if __name__ == "__main__":
    file_path = os.path.join('inputs', 'day14.txt')
    print(part1(file_path))
    print(part2(file_path))