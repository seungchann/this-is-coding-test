n,m = map(int, input().split())
num_list = list(min(list(map(int, input().split()))) for i in range(n))
print(max(num_list))