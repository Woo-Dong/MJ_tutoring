"""
백준 - 1427번(소트인사이드)
https://www.acmicpc.net/problem/1427

문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""
"""
백준 - 11004번(K번째 수)

문제
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

출력
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
"""

def _quick_sort(data, start, end):
    pivot = start
    partition = start + 1
    for i in range(start+1, end+1):
        if data[pivot] <= data[i]:
            data[i], data[partition] = data[partition], data[i]
            partition += 1
    partition -= 1
    data[pivot], data[partition] = data[partition], data[pivot]

    return partition

def quick_sort(data, start=0, end=None):

    if end is None:
        end = len(data) - 1

    if end - start < 1:
        return
    pivot = _quick_sort(data, start, end)

    quick_sort(data, start, pivot-1)
    quick_sort(data, pivot+1, end)

input_list = list(map(int, input()))

quick_sort(input_list)
print(''.join(map(str, input_list)))

