"""
BaekJoon - 1915번(가장 큰 정사각형)
https://www.acmicpc.net/problem/1915 

문제
n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.
0	1	0	0
0	1	1	1
1	1	1	0
0	0	1	0
위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다. 

입력
첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

출력
첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.
"""

from copy import deepcopy as dcp
n, m = map(int, input().split()) 
alist = list() 
for _ in range(n): 
    alist.append(list(map(int, input())))

dp_arr = dcp(alist)  
ans = dp_arr[0][0] # (1, 1)부터 탐색할 것이므로 범위에 없는 (0, 0)을 초기값으로 저장.

for i in range(1, n): 
    for j in range(1, m): 
        if alist[i][j]: # 정사각형의 맨 오른쪽 아래 모서리를 포함한 정사각형의 최대 크기를 저장
            # 해당 영역의 왼쪽 위쪽, 대각선 위쪽의 값중 
            # 가장 최솟값이 곧 1로만 이루어진 정사각형 크기의 최댓값이므로 해당 크기 +1을 더함
            dp_arr[i][j] = min(dp_arr[i-1][j], dp_arr[i][j-1], dp_arr[i-1][j-1]) + 1 
        ans = max(ans, dp_arr[i][j]) # 매번마다 가장 큰 크기를 저장.

print(ans * ans)  # 최댓값의 넓이를 출력