def read_input():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        entries = [(list(x.split(" ")[0]), [int(y) for y in x.split(" ")[-1].split(",")]) for x in lines]

        return entries

def is_valid(chain, groups):
    actual_groups = []
    last_group = 0
    for element in chain:
        if element == "#":
            last_group += 1
        if element == ".":
            if last_group != 0:
                actual_groups.append(last_group)
            last_group = 0
    if last_group != 0:
        actual_groups.append(last_group)
    # check if actual_groups is same as groups
    # print("Comparing ", actual_groups, groups)
    if len(actual_groups) != len(groups):
        return False
    return all(x == y for x, y in zip(actual_groups, groups))

def backtrack(partial_chain, chain, groups):
    # TODO partial check not to go until the end

    if len(partial_chain) == len(chain):
        # Deciding if it's a valid solution
        if is_valid(partial_chain, groups):
            return 1
        else:
            return 0

    next_idx = len(partial_chain)
    if chain[next_idx] == "?":
        return backtrack(partial_chain + ["#"], chain, groups) + backtrack(partial_chain + ["."], chain, groups)
    else:
        return backtrack(partial_chain + [chain[next_idx]], chain, groups)



def solve_entry(entry):
    chain = entry[0]
    groups = entry[1]

    return backtrack([], chain, groups)


def solve(entries):
    ans = sum(solve_entry(entry) for entry in entries)
    return ans


entries = read_input()

print(solve(entries))
