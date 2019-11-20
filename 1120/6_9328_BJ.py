"""
BaekJoon - 9328번(열쇠)
https://www.acmicpc.net/problem/9328

문제
상근이는 1층 빌딩에 침입해 매우 중요한 문서를 훔쳐오려고 한다. 상근이가 가지고 있는 평면도에는 문서의 위치가 모두 나타나 있다. 빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요하다. 상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다.

상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

각 테스트 케이스의 첫째 줄에는 지도의 높이와 너비 h와 w (2 ≤ h, w ≤ 100)가 주어진다. 다음 h개 줄에는 빌딩을 나타내는 w개의 문자가 주어지며, 각 문자는 다음 중 하나이다.

'.'는 빈 공간을 나타낸다.
'*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
'$'는 상근이가 훔쳐야하는 문서이다.
알파벳 대문자는 문을 나타낸다.
알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.
마지막 줄에는 상근이가 이미 가지고 있는 열쇠가 공백없이 주어진다. 만약, 열쇠를 하나도 가지고 있지 않는 경우에는 "0"이 주어진다.

상근이는 빌딩 밖으로 나갈 수 있다. 각각의 문에 대해서, 그 문을 열 수 있는 열쇠의 개수는 0개, 1개, 또는 그 이상이고, 각각의 열쇠에 대해서, 그 열쇠로 열 수 있는 문의 개수도 0개, 1개, 또는 그 이상이다. 열쇠는 여러 번 사용할 수 있다.

출력
각 테스트 케이스 마다, 상근이가 훔칠 수 있는 문서의 최대 개수를 출력한다.
"""

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