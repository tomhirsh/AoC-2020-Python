import os
import numpy as np

directions = {'N': np.array([0,1]) ,'S':np.array([0,-1]), 'E':np.array([1,0]), 'W':np.array([-1,0])}
moves = {'L', 'R', 'F'}

def manhatten(file_path, start_loc=(0.,0.), angle=0):
    cur_pos = np.array(start_loc)
    
    with open (file_path, 'r') as f:
        for line in f:
            move = line[0]
            val = float(line[1:-1])
            if move in directions.keys():
                dir = np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))])
                cur_pos += directions[move] * val
            else:
                if move == 'R':
                    angle = (angle + val) % 360
                elif move == 'L':
                    angle = (angle - val) % 360
                dir = np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))])
                if move == 'F':
                    dir = np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))])
                    cur_pos += dir*val
    return np.linalg.norm(cur_pos, ord=1)


def manhatten2(file_path, start_loc=(0.,0.), waypoint=(0.,0.)):
    cur_pos = np.array(start_loc)
    waypoint = np.array(waypoint)
    
    with open (file_path, 'r') as f:
        for line in f:
            move = line[0]
            val = float(line[1:-1])
            if move in directions.keys():
                waypoint += directions[move] * val
            else:

                if move == 'F':
                    cur_pos += val * waypoint
                else:
                    if move == 'L':
                        val *= -1
                    rot_mat = np.array([[np.cos(np.deg2rad(val)), np.sin(np.deg2rad(val))],
                                        [-np.sin(np.deg2rad(val)), np.cos(np.deg2rad(val))]])
                    waypoint = rot_mat @ waypoint

    return np.linalg.norm(cur_pos, ord=1)


if __name__ == "__main__":
    file_path = os.path.join('inputs','day12.txt')
    print(round(manhatten(file_path, start_loc=(0.,0.), angle=0)))
    print(round(manhatten2(file_path, start_loc=(0.,0.), waypoint=(10.,1.))))
