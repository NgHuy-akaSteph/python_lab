# THỐNG KÊ DỊCH TỄ - LOANG
#C1 : Dùng mảng visited đánh dấu những nguy cơ đã duyệt
path = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
res = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:  # bệnh nhân
            for x, y in path:
                i1, j1 = i + x, j + y
                if 0 <= i1 < n and 0 <= j1 < m and a[i1][j1] >= 0:
                    if not visited[i1][j1]:
                        res += a[i1][j1]
                        visited[i1][j1] = True

print(res)

# C2: Đổi luôn các nguy cơ đã duyệt thành 0
n, m = map(int, input().split())
s = 0
a, q = [], []
dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(m):
        if row[j] == -1:
            q.append((i,j))

while q:
    u = q.pop()
    for dx, dy in dirs:
        x, y = u[0] + dx, u[1] + dy
        if 0 <= x < n and 0 <= y < m:
            s += a[x][y]
            a[x][y] = 0
print(s)

