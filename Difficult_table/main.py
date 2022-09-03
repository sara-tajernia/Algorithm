def findPath(i, j, mat, dp):

    x, y, z, w,p,q,r,s = -1, -1, -1, -1,-1,-1,-1,-1

    if j < n - 1 and chr(ord(mat[i][j]) + 1) == chr(ord(mat[i][j + 1])):            #E
        x = 1 + findPath(i, j + 1, mat, dp)

    if j > 0 and chr(ord(mat[i][j]) +1)  == chr(ord(mat[i][j - 1])):                #W
        y = 1 + findPath(i, j - 1, mat, dp)

    if i > 0 and chr(ord(mat[i][j]) +1) == chr(ord(mat[i - 1][j])):                 #S
        z = 1 + findPath(i - 1, j, mat, dp)

    if i < m - 1 and chr(ord(mat[i][j]) +1) == chr(ord(mat[i + 1][j])):             #N
        w = 1 + findPath(i + 1, j, mat, dp)

    if j < n - 1 and i < m-1 and chr(ord(mat[i][j]) +1) == chr(ord(mat[i + 1][j + 1])):         #NE
        p = 1 + findPath(i + 1, j + 1, mat, dp)

    if j > 0 and i >0 and chr(ord(mat[i][j]) +1)  == chr(ord(mat[i - 1][j - 1])):               #SW
        q = 1 + findPath(i - 1, j - 1, mat, dp)

    if i > 0 and j < n - 1 and chr(ord(mat[i][j]) +1) == chr(ord(mat[i - 1][j + 1])):           #SE
        r = 1 + findPath(i - 1, j + 1, mat, dp)

    if i < m - 1 and j > 0 and  chr(ord(mat[i][j]) +1) == chr(ord(mat[i + 1][j - 1])):          #NW
        s = 1 + findPath(i + 1, j - 1, mat, dp)


    dp[i][j] = max(x, max(y, max(z, max(w, max(p, max(q, max(r, max(s, 1))))))))
    return dp[i][j]


def finLongest(mat, letter):
    dp = [[-1 for i in range(n)] for i in range(m)]
    x = -1
    y = -1
    maximum = 0
    for i in range(m):
        for j in range(n):
            if (dp[i][j] == -1) and mat[i][j] == letter:
                findPath(i, j, mat, dp)
    for k in range(m):
        for l in range(n):
            if dp[k][l] > maximum:
                maximum = dp[k][l]
                x = k
                y = l
    print(maximum, '\n', x,' ', y, sep='')

if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    mat = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        data = input().split()
        for j in range(n):
            mat[i][j] = data[j]
    letter = input()

    finLongest(mat, letter)