from itertools import combinations

n = int(input())
#input()은 입력된 값을 다 str로 받음
#print(type(n))
taste = []
combination = []
result = 9999

for _ in range(n):
  taste.append(list(map(int, input().split())))
#.split()있어야 함 taste.append(list(map(int, input().split())))
#.split()있어야 함

for i in range(0,n):
  combination.append(i)

combi_result = []
for i in range(1,n+1):
  for c in combinations(combination,i):
      combi_result.append(c)

for combi in combi_result:
  mul = 1
  sum_num = 0
  for j in combi:
    mul = mul * taste[j][0]
    sum_num = sum_num + taste[j][1]
  result = min(result,abs(mul-sum_num))
#if result ==1
# break
print(result)
