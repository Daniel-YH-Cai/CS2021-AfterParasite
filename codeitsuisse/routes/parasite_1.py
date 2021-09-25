import numpy

def parasiteP1(grid, tar):
    queue = []
    height = len(grid)
    width = len(grid[0])
    tarX, tarY = int(tar.split(',')[0]), int(tar.split(',')[1])
    startX, startY = findStart(grid)
    visited = numpy.zeros((len(grid), len(grid[0]), 2))
    queue.append((startX, startY))
    visited[startX][startY][0] = 0
    visited[startX][startY][1] = 0
    while len(queue) != 0:
        curX, curY = queue.pop(0)
        if curX - 1 >= 0 and visited[curX-1][curY][0] == 0 and grid[curX-1][curY] == 1:
            if curX - 1 == tarX and curY == tarY:
                return visited[curX][curY][1]+1
            visited[curX-1][curY][0] = 1
            visited[curX-1][curY][1] = visited[curX][curY][1]+1
            queue.append((curX-1, curY))
        if curY - 1 >= 0 and visited[curX][curY-1][0] == 0 and grid[curX][curY-1] == 1:
            if curX == tarX and curY - 1 == tarY:
                return visited[curX][curY][1]+1
            visited[curX][curY-1][0] = 1
            visited[curX][curY-1][1] = visited[curX][curY][1]+1
            queue.append((curX, curY-1))
        if curX + 1 < height and visited[curX+1][curY][0] == 0 and grid[curX+1][curY] == 1:
            if curX + 1 == tarX and curY == tarY:
                return visited[curX][curY][1]+1
            visited[curX+1][curY][0] = 1
            visited[curX+1][curY][1] = visited[curX][curY][1]+1
            queue.append((curX+1, curY))
        if curY + 1 < width and visited[curX][curY+1][0] == 0 and grid[curX][curY+1] == 1:
            if curX == tarX and curY + 1 == tarY:
                return visited[curX][curY][1]+1
            visited[curX][curY+1][0] = 1
            visited[curX][curY+1][1] = visited[curX][curY][1]+1
            queue.append((curX, curY+1))
    return -1


def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 3):
                return [i, j]


def main():
    grid1 = [[0, 3, 2],
            [0, 1, 1],
            [1, 0, 0]]
    grid2 = [[0, 1, 0, 1],
             [2, 3, 2, 1],
             [0, 1, 0, 0],
             [1, 0, 0, 1]]
    tar1 = '1,1'
    tar2 = '2,1'
    print(parasiteP1(grid1, tar1))
    print(parasiteP1(grid2, tar2))

if __name__ == '__main__':
    main()
