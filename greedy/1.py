from sys import stdin

n,m,k = map(int, stdin.readline().split())
num_list = list(map(int, stdin.readline().split()))
answer = 0

num_list.sort(reverse=True)

while(m>1):
    for _ in range(0,k):
        answer += num_list[0]
        m -= 1
    answer += num_list[1]
    m -= 1
    
print(answer)