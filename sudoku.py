grid = [[1,2,3,0,5,6,0,8,9],
[4,5,6,7,8,9,1,2,3],
[0,6,9,5,0,5,4,8,9],
[0,0,8,9,5,0,6,4,0],
[9,0,5,3,2,7,8,8,9],
[8,4,4,0,0,8,9,9,0],
[9,6,0,7,5,8,0,6,4],
[7,8,9,4,0,4,0,6,0],
[0,2,3,1,5,0,4,7,8]]

def n_valide(y, x, n):
    global grid
    #on determine si le nombre invalide est sur sa ligne
    for x0 in range(len(grid)):
        if grid[y][x0] == n:
            return False
        # on determine si le nombre est valide par sa colonne
        for y0 in range(len(grid)):
            if grid[y0][x] == n:
                return False
        # on determine si le nombre est valide par sa sous grille
        # x0 et y0 vont ns données les points de depart d'une sous grille

        x0 =(x//3) * 3
        y0 = (y// 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == n:
                    return False
        return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if n_valide(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
solve()