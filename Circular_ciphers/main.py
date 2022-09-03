#complex password
rows, columns = list(map(int, input().split()))
matrix = [[0] * columns for i in range(rows)]
for i in range(rows):
    matrix[i] = input().split()

h = int(input())
instruction = input().split()
t = int(input())
answer = []
for i in range (rows):
    answer.append(0)

count = 0
while count<t:
    answer[count%rows] += int(instruction[count%h])
    count +=1
save = []
for i in range (rows):
    if i<t%rows:
        save.append(int(matrix[i][int(answer[i] % columns)]))
    else:
        print(int(matrix[i][int(answer[i]%columns)]), end='')

for i in range (len(save)):
    print(save[i], end='')