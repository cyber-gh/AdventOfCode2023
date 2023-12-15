import pprint


def read_input_char_matrix():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        char_matrix = [list(line) for line in lines]
        return char_matrix


def expand_universe(universe):
    rows_with_no_galaxies = [i for i in range(len(universe)) if "#" not in universe[i]]
    columns_with_no_galaxies = [i for i in range(len(universe[0])) if "#" not in [x[i] for x in universe]]

    # duplicate every row with no galaxies
    new_universe = []
    for row in range(len(universe)):
        new_universe.append(universe[row])
        if row in rows_with_no_galaxies:
            new_universe.append(universe[row])

    # duplicate every column with no galaxies
    new_universe = [[new_universe[i][j] for j in range(len(new_universe[0]))] for i in range(len(new_universe))]
    column_offset = 0
    for column in range(len(new_universe[0])):
        if column in columns_with_no_galaxies:
            for i in range(len(new_universe)):
                new_universe[i].insert(column + column_offset, ".")
            column_offset += 1

    return new_universe

def print_universe(universe):
    for row in universe:
        print("".join(row))

    print("------------------")
    print("------------------")

def calculate_dist(universe):
    galaxies = [(i, j) for i in range(len(universe)) for j in range(len(universe[0])) if universe[i][j] == "#"]

    # calculate euclidian distance between each pair of galaxies
    ans = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            print("Dist between", i + 1, "and", j + 1, "is", dist)
            ans += dist

    return ans

universe = read_input_char_matrix()

print_universe(universe)

universe = expand_universe(universe)

print_universe(universe)

print(calculate_dist(universe))
