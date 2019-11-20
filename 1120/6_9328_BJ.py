
from collections import deque 
import sys
sys.stdin = open('input_data.txt', 'r') 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

TC = int(input()) 
for _ in range(TC): 
    h, w = map(int, input().split()) 
    arr = list() 
    for _ in range(h):
        arr.append(input()) 
    keys = set(input())

    entrance, doors, candidate_entr = list(), list(), list() 
    ans = 0 
    for i in [0, h-1]:
        for j in range(w):
            if arr[i][j] == '.':
                entrance.append((i, j))
            elif arr[i][j] == '$':
                entrance.append((i, j))
            elif arr[i][j] != '*':
                char = arr[i][j] 
                if char.isupper():
                    doors.append((i, j, arr[i][j]))
                    candidate_entr.append((i, j))
                elif char.islower():
                    keys.add(char)
                    entrance.append((i, j))  

    for j in [0, w-1]:
        for i in range(1, h-1):
            if arr[i][j] == '.': entrance.append((i, j))
            elif arr[i][j] == '$':
                entrance.append((i, j))
            elif arr[i][j] != '*':
                char = arr[i][j] 
                if char.isupper():
                    doors.append((i, j, arr[i][j]))
                    candidate_entr.append((i, j))
                elif char.islower():
                    keys.add(char)
                    entrance.append((i, j))  

    for x, y in candidate_entr:
        char = arr[x][y]
        if char.lower() in keys: entrance.append((x, y)) 

    check = [ [False] * w for _ in range(h) ]
    for x, y in entrance: check[x][y] = True 
    queue = deque(entrance)

    while queue: 
        x, y = queue.popleft() 
        if arr[x][y] == '$': ans += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i] 

            if 0 <= nx < h and 0 <= ny < w:
                if check[nx][ny] or arr[nx][ny] == '*': continue
                elif arr[nx][ny] == '.':
                    queue.append((nx, ny)) 
                    check[nx][ny] = True 
                elif arr[nx][ny] == '$':
                    queue.append((nx, ny))
                    check[nx][ny] = True 
                else: 
                    char = arr[nx][ny] 
                    if char.isupper(): 
                        if char.lower() in keys:
                            queue.append((nx, ny)) 
                            check[nx][ny] = True 
                        else:
                            doors.append((nx, ny, arr[nx][ny])) 
                            check[nx][ny] = True
                    elif char.islower():
                        keys.add(char) 
                        queue.append((nx, ny))
                        check[nx][ny] = True 
                        for kx, ky, code in doors: 
                            if code.lower() in keys: 
                                queue.append((kx, ky)) 
                                check[kx][ky] = True
    print(ans) 