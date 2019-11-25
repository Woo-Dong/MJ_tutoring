"""
BaekJoon - 1463번(1로 만들기)
https://www.acmicpc.net/problem/1463

문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""

n = int(input()) 
MAX = 10e6
dp_arr = [MAX] * (n+1)  # 저장할 값: 해당 숫자가 오기까지의 최소 횟수 저장.
dp_arr[1] = 0 
for i in range(1, n): 
    if i*2 <= n:    # 2의 배수일 경우 1 추가, 단 3의 배수일 경우일 수도 있으므로 최소값으로 저장.
        dp_arr[i*2] = min(dp_arr[i*2], dp_arr[i] + 1)
    if i*3 <= n:    # 3의 배수일 경우 1 추가, 이하 동일
        dp_arr[i*3] = min(dp_arr[i*3], dp_arr[i] + 1)
    dp_arr[i+1] = min(dp_arr[i+1], dp_arr[i] + 1)   # 다음 값으로 옮길 경우 계산.

print(dp_arr[n]) 