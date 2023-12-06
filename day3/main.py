import pprint

def check_around(matrix, i, j):
    print("check_around " + str(i) + " " + str(j))
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    n = len(matrix)
    m = len(matrix[0])

    for d in range(len(dx)):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < n and 0 <= y < m:
            print(str(x) + " " + str(y) + " " + str(matrix[x][y]))
            if matrix[x][y] != "." and (not matrix[x][y].isdigit()):
                return True
    print("-----")
    return False

def solve(matrix):
    ans = 0
    pprint.pprint(matrix)
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[0]):
            element = matrix[i][j]
            if element.isdigit():
                nr_raw = ""
                last_z = j
                for z in range(j, len(matrix[0])):
                    if matrix[i][z].isdigit():
                        nr_raw += matrix[i][z]
                        last_z = z
                    else:
                        break
                nr = int(nr_raw)
                print(str(j) + " " + str(last_z))
                has_symbol = any(check_around(matrix, i, x) for x in range(j, last_z + 1))
                if has_symbol:
                    ans += nr
                print(str(nr) + " " + str(has_symbol))
                j = last_z + 1
            else:
                j += 1
    return ans

matrix = [[x for x in y.replace("\n","")] for y in open("input.txt", "r").readlines()]

print(solve(matrix))
