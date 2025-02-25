# 1
# Ответ: True
# 2
a = input()
c = input()
print(a == c)
# Ответ: False
# 3
a = []
for i in range(4):
    a.append(int(input()))
print(min(a))
# Ответ: 5
# 4
a = []
for i in range(4):
    a.append(int(input()))
print(max(a))
# Ответ: 30
# 5
a = []
for i in range(3):
    a.append(int(input()))
max_st = max(a)
sum_st = 0
for i in a:
    if i != max_st:
        sum_st += i
print(sum_st > max_st)
# Ответ: True
# 6
a = []
for i in range(3):
    a.append(int(input()))
max_st = max(a)
sum_st = 0
for i in a:
    if i != max_st:
        sum_st += i
if sum_st == max_st:
    print('вырожденный')
elif a[0] == a[1] == a[2]:
    print('равносторонний')
elif a[0] != a[1] != a[2]:
    print('разносторонний')
# Ответ: вырожденный
# 7
a = []
for i in range(4):
    a.append(int(input()))
sum_st = 0
for i in range(a[2], a[1]+1):
    sum_st += 1    
print(sum_st)
# Ответ: 7
