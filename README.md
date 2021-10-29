# sudokugrid = [[0, 7, 2, 9, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 6, 0, 8, 0],
        [0, 0, 0, 0, 4, 0, 0, 6, 0],
        [9, 6, 0, 0, 0, 4, 1, 0, 8],
        [0, 4, 8, 7, 0, 5, 0, 9, 6],
        [0, 0, 5, 6, 0, 8, 0, 0, 3],
        [0, 0, 0, 4, 0, 2, 0, 1, 0],
        [8, 5, 0, 0, 6, 0, 3, 2, 7],
        [1, 0, 0, 8, 5, 0, 0, 0, 0]]


def n_valide(y, x, n): # quand on place un nombre sur une case on regarde les lignes et les colones si on peut le placé
    global grid
    # on determine si le nombre invalide est sur sa ligne
    for x0 in range(9):
        if grid[y][x0] == n:
            return False
        # on determine si le nombre est valide par sa colonne
        for y0 in range(9):
            if grid[y0][x] == n:
                return False
        # on determine si le nombre est valide par sa sous grille
        # x0 et y0 vont ns données les points de depart d'une sous grille

    # x0 =(x//3) * 3
    # y0 = (y// 3) * 3
    x0 = x // 3
    y0 = y // 3
    for i in range(y0 * 3, y0 * 3 + 3):
        for j in range(x0 * 3, x0 * 3 + 3):
            if grid[i][j] == n and (i, j) != (y, x):
                return False

    return True


def solve():
    global grid
    for y in range(9):# parcour les lignes
        for x in range(9):# parcour les colonnes
            if grid[y][x] == 0: # case a resoudre
                for n in range(1, 10):
                    if n_valide(y, x, n):
                        grid[y][x] = n
                        if solve():
                            return True
                        grid[y][x] = 0
                return  # si on rien trouver au boucle et on depile
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


solve()

for row in grid:
    print(row)
