# Given a 2d grid of 1s (land) and 0s (water), count the number of islands. 
# An island is a group of 1s connected horizontally or vertically.

import random 
import time
from collections import deque

def create_map(rows, cols):
    map = [[0 for i in range(cols)] for j in range(rows)]
    random.seed()

    for m in range(0, rows):
        for n in range(0, cols):
            map[m][n] = random.randint(0,1)
    
    return map

def print_map(map):
    for m in range(len(map)):
        for n in range(len(map[0])):
            print("\U0001F7E6" if map[m][n] == 0 else "\U0001F7E8", end=" ")
        print('')

def print_visited(map):
    for m in range(len(map)):
        for n in range(len(map[0])):
            print("\U0001F7E6" if map[m][n] == True else "\U0001F7E8", end=" ")
        print('')

def main():
    rows = 15
    cols = 15
    delta_t = 0.05
    should_print = rows < 30 and cols < 30

    
    map = create_map(rows, cols)
    start_time = time.perf_counter()

    isVisited = [[False for i in range(cols)] for j in range(rows)]

    islands = 0
    for m in range(0, rows):
        for n in range(0, cols):
            if (not isVisited[m][n]):
                if map[m][n] == 0:
                    isVisited[m][n] = True
                else:
                    # hit an island
                    islands += 1

                    q = deque()
                    q.append((m,n))

                    while (len(q) > 0):
                        current = q.pop()
                        x = current[0]
                        y = current[1]

                        isVisited[x][y] = True

                        if (should_print):
                            print("\033c", end="", flush=True)
                            print_visited(isVisited)
                            time.sleep(delta_t)

                        # visit neighbors

                        right = (x, y+1)
                        up = (x-1, y)
                        down = (x + 1, y)
                        left = (x, y-1)

                        neighbors = [right, up, down, left]

                        for neighbor in neighbors:
                            if neighbor[0] >= 0 and neighbor[0] < rows and neighbor[1] >= 0 and neighbor[1] < cols:
                                if not isVisited[neighbor[0]][neighbor[1]] and map[neighbor[0]][neighbor[1]]:
                                    q.append(neighbor)

    if (should_print):
        print("\033c", end="", flush=True)
        print_map(map)
        print()
    print('Program completed finding ' + str(islands) + ' islands')
    end_time = time.perf_counter()
    print("Elapsed " + str((end_time - start_time)) + ' seconds')

if __name__ == "__main__":
    main()