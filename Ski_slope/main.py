from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class queueNode:
    def __init__(self, pt, dist):
        self.pt = pt
        self.dist = dist

def BFS(mat, src, dest):
    visited = [[False for i in range(COL)]for j in range(ROW)]
    visited[src.x][src.y] = True
    Q = deque()
    Q.append(queueNode(src, 0))
    rows = [-1, 0, 0, 1]
    cols = [0, -1, 1, 0]

    while Q:
        curr = Q.popleft()
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist

        for i in range(4):
            row = pt.x + rows[i]
            col = pt.y + cols[i]
            if ((row >= 0) and (row < ROW) and (col >= 0) and (col < COL) and
                    (mat[row][col] == 'M' or mat[row][col] == 'O')and not visited[row][col]):
                visited[row][col] = True
                Q.append(queueNode(Point(row, col), curr.dist + 1))
    return -1


if __name__ == '__main__':

    ROW, COL = list(map(int, input().split()))
    mat = [[0 for i in range(COL)] for j in range(ROW)]
    for i in range(ROW):
        data = input()
        for j in range(COL):
            mat[i][j] = data[j]

    answer = [[-1 for i in range(COL)] for j in range(ROW)]
    listM, listO = [], []
    for i in range(ROW):
        for j in range(COL):
            if mat[i][j] == 'M':
                answer[i][j] = 0
                listM.append(Point(i, j))
            elif mat[i][j] == 'O':
                listO.append(Point(i, j))

    for i in range(len(listO)):
        distance = COL * ROW
        for j in range(len(listM)):
            dist = BFS(mat, listO[i], listM[j])
            if dist < distance and dist > 0:
                distance = dist
                answer[listO[i].x][listO[i].y] = distance

    for i in range(ROW):
        print(' '.join(map(str, answer[i])))