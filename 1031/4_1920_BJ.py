"""
백준 - 1920번(수 찾기)
https://www.acmicpc.net/problem/1920

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수들의 범위는 int 로 한다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""

N = int(input())
a_list = list(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))

a_list.sort()

for find in find_list:
    left, right = 0, N-1
    included = False
    while True:
        mid = (left+right) // 2
        target = a_list[mid] # 인덱스 접근을 통한 해당 값의 이분탐색.
        if target == find:  # target이 있는지 확인
            included = True
            break

        if left == right: break # 전부 탐색하였으면 break
        elif target < find: left = mid + 1 # 찾는 값이 현재 값보다 크다면 오른쪽으로 범위를 좁힘
        else: right = mid  # 찾는 값이 현재 값보다 작다면 왼쪽으로 범위를 좁힘

    if included:
        print(1)
    else:
        print(0)

