"""
백준 - 2110번(공유기 설치)
https://www.acmicpc.net/problem/2110

문제
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (1 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
"""

N, C = map(int, input().split())

ipTime = list()
for _ in range(N):
    ipTime.append(int(input()))

ipTime.sort()
left = ipTime[1] - ipTime[0]
right = ipTime[-1] - ipTime[0]

ans = 0

while left <= right:

    gap = (left+right) // 2  # 가장 인접한 두 공유기 사이의  최대 거리를 이분 탐색
    cnt = 1
    tmp = ipTime[0]         # 맨 앞에 공유기를 설치하는 경우가 최적의 해.
    for i in range(1, N):    
        if ipTime[i] >= tmp + gap: # gap 범위 밖에 있을 경우 공유기를 설치할 수 있다.
            tmp = ipTime[i]        
            cnt += 1                
    if cnt >= C:            # C개 이상의 공유기를 설치할 수 있는 경우 gap을 늘린다. 
        left = gap + 1      # 최대거리를 구하기 위해 다시 반복.
        ans = gap           
    else:                   # C개 이상 설치할 수 없는 경우 gap을 줄인다.
        right = gap - 1
print(ans)