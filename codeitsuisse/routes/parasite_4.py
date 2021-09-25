import numpy

def parasiteP4(grid):
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
        if (curX - 1 >= 0):
            energy = visited[curX][curY][1] if grid[curX - 1][curY] == 1 else visited[curX][curY][1]+1
            if visited[curX-1][curY][0] != 1:
                visited[curX-1][curY][0] = 1
                visited[curX-1][curY][1] = energy
                queue.append((curX-1, curY))
            elif visited[curX-1][curY][1] > energy:
                visited[curX-1][curY][1] = energy
        if (curX + 1 < height):
            energy = visited[curX][curY][1] if grid[curX+1][curY] == 1 else visited[curX][curY][1]+1
            if visited[curX+1][curY][0] != 1:
                visited[curX+1][curY][0] = 1
                visited[curX+1][curY][1] = energy
                queue.append((curX+1, curY))
            elif visited[curX+1][curY][1] > energy:
                visited[curX+1][curY][1] = energy
        if (curY - 1 >= 0):
            energy = visited[curX][curY][1] if grid[curX][curY-1] == 1 else visited[curX][curY][1]+1
            if visited[curX][curY-1][0] != 1:
                visited[curX][curY-1][0] = 1
                visited[curX][curY-1][1] = energy
                queue.append((curX, curY-1))
            elif visited[curX][curY-1][1] > energy:
                visited[curX][curY-1][1] = energy
        if (curY + 1 < width):
            energy = visited[curX][curY][1] if grid[curX][curY+1] == 1 else visited[curX][curY][1]+1
            if visited[curX][curY+1][0] != 1:
                visited[curX][curY+1][0] = 1
                visited[curX][curY+1][1] = energy
                queue.append((curX, curY+1))
            elif visited[curX][curY+1][1] > energy:
                visited[curX][curY+1][1] = energy
    max = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1 and visited[i][j][1] > max:
                max = visited[i][j][1];
    return int(max)
        

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
    grid3 = [[0, 1, 0, 1],
             [2, 3, 2, 1],
             [0, 1, 0, 0],
             [1, 0, 0, 1]]
    tar1 = '0,0'
    tar2 = '1,1'
    tar3 = '2,1'
    print(parasiteP4(grid1))
    print(parasiteP4(grid2))
    print(parasiteP4(grid3))

if __name__ == '__main__':
    main()