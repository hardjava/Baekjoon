from collections import deque

def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    start = (0, 0)
    end = (len(maps) - 1, len(maps[0]) - 1)
    d = deque([start])

    while d:
        row, col = d.popleft()
        for i in range(4):
            nx = col + dx[i]
            ny = row + dy[i]

            if (0 <= nx < len(maps[0])) and (0 <= ny < len(maps)):
                if maps[ny][nx] == 1  and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[row][col] + 1
                    d.append((ny, nx))

    if visited[end[0]][end[1]] == False:
        return -1
    else:
        return maps[end[0]][end[1]]