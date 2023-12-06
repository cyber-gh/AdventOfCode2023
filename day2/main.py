

def solve_game(game_str):
    game_id, game_raw = game_str.split(':')
    game_id = int(game_id.strip().split(' ')[1])

    games = game_raw.replace(";",",").split(',')
    games = [x.strip() for x in games]
    games = [(int(x.split(" ")[0]), x.split(" ")[1]) for x in games]

    if any(x[1] == "blue" and x[0] > 14 for x in games):
        return 0
    if any(x[1] == "green" and x[0] > 13 for x in games):
        return 0
    if any(x[1] == "red" and x[0] > 12 for x in games):
        return 0

    return game_id

input_lines = [x.replace("\n","") for x in open("input.txt", "r").readlines()]

ans = sum([solve_game(x) for x in input_lines])

print(ans)
