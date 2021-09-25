import numpy

def parasiteP2(grid):
    queue = []
    height = len(grid)
    width = len(grid[0])
    startX, startY = findStart(grid)
    visited = numpy.zeros((height, width, 2))
    queue.append((startX, startY))
    visited[startX][startY][0] = 0
    visited[startX][startY][1] = 0
    while len(queue) != 0:
        curX, curY = queue.pop(0)
        if curX - 1 >= 0 and visited[curX-1][curY][0] == 0 and grid[curX-1][curY] == 1:
            visited[curX-1][curY][0] = 1
            visited[curX-1][curY][1] = visited[curX][curY][1]+1
            queue.append((curX-1, curY))
        if curY - 1 >= 0 and visited[curX][curY-1][0] == 0 and grid[curX][curY-1] == 1:
            visited[curX][curY-1][0] = 1
            visited[curX][curY-1][1] = visited[curX][curY][1]+1
            queue.append((curX, curY-1))
        if curX + 1 < height and visited[curX+1][curY][0] == 0 and grid[curX+1][curY] == 1:
            visited[curX+1][curY][0] = 1
            visited[curX+1][curY][1] = visited[curX][curY][1]+1
            queue.append((curX+1, curY))
        if curY + 1 < width and visited[curX][curY+1][0] == 0 and grid[curX][curY+1] == 1:
            visited[curX][curY+1][0] = 1
            visited[curX][curY+1][1] = visited[curX][curY][1]+1
            queue.append((curX, curY+1))
    # print(len(visited),len(visited[0]))
    # print(visited)
    ans = 0
    for i in range(height):
        for j in range(width):
            if visited[i][j][0] == 0 and grid[i][j] == 1:
                return -1
            if visited[i][j][1] > ans and grid[i][j] == 1:
                ans = visited[i][j][1]
    return ans

def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 3):
                return [i, j]


def main():
    grid1 = [[0, 3], [0, 1]]
    grid2 = [[0, 3, 2],
            [0, 1, 1],
            [1, 0, 0]]
    grid3 = [[0, 1, 1, 1],
             [2, 3, 2, 1],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
    tar1 = '0,0'
    tar2 = '1,1'
    tar3 = '2,1'
    print(parasiteP2(grid1))
    print(parasiteP2(grid2))
    print(parasiteP2(grid3))

if __name__ == '__main__':
    main()