
from collections import deque 

import sys
sys.stdin = open('input_data.txt', 'r') 

# Setting directions 
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
    
    # 테두리 부분에 입구 확인
    ans = 0 
    for i in [0, h-1]:
        for j in range(w): # 가로 벽 먼저 확인
            if arr[i][j] == '.' or arr[i][j] == '$': # 빈 공간이거나 문서가 있는 경우
                entrance.append((i, j))
            elif arr[i][j] != '*': # 벽이 아니라면 문자이므로 문 또는 키
                char = arr[i][j] 
                if char.isupper(): # 문일 경우
                    doors.append((i, j, arr[i][j]))
                    candidate_entr.append((i, j))
                elif char.islower(): # 키일 경우 
                    keys.add(char)
                    entrance.append((i, j))  

    for j in [0, w-1]:
        for i in range(1, h-1): # 똑같이 세로 벽에 확인
            if arr[i][j] == '.' or arr[i][j] == '$':
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
        if char.lower() in keys: entrance.append((x, y)) # 테두리에 있는 문 중에서 키가 있는 문은 입구로 지정

    check = [ [False] * w for _ in range(h) ] # 해당 영역을 탐색했는지 확인하는 리스트
    for x, y in entrance: check[x][y] = True # 테두리의 입구는 모두 탐색했다고 설정.
    queue = deque(entrance) # deque 선언 -> BFS 탐색할 대상

    while queue: # 더이상 탐색범위가 없을 경우 종료.
        x, y = queue.popleft() # 큐에서 하나씩 빼서
        if arr[x][y] == '$': ans += 1 # 문서일 경우 정답에 1 추가
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i] # 동서남북 방향으로 탐색

            if 0 <= nx < h and 0 <= ny < w: # 인덱스 범위 내라면,
                if check[nx][ny] or arr[nx][ny] == '*': continue # 이미 탐색한 경우나 벽일 경우 다음 방향으로.
                elif arr[nx][ny] == '.': # 주변 영역이 빈공간일 경우 탐색 범위 추가
                    queue.append((nx, ny)) 
                    check[nx][ny] = True 
                elif arr[nx][ny] == '$': # 문서일경우 이하 동일.
                    queue.append((nx, ny))
                    check[nx][ny] = True 
                else: 
                    char = arr[nx][ny] 
                    if char.isupper(): # 문일 경우,
                        if char.lower() in keys: # 키에 포함된다면
                            queue.append((nx, ny)) # 탐색범위 추가
                            check[nx][ny] = True 
                        else:
                            doors.append((nx, ny, arr[nx][ny]))  # 키에 없으면 임시로 리스트에 위치와 문 종류 저장
                            check[nx][ny] = True
                    elif char.islower(): # 키일 경우 
                        keys.add(char) # 키의 set에 일단 추가.
                        queue.append((nx, ny))
                        check[nx][ny] = True 
                        for kx, ky, code in doors: # 임시로 문의 위치와 종류를 저장한 리스트에서 탐색하여
                            if code.lower() in keys: # 일치하는 문이 있을 경우
                                queue.append((kx, ky)) # 그 문의 위치를 탐색범위에 추가.
                                check[kx][ky] = True
    print(ans) 