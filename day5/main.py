
def read_input():
    with open('input.txt', 'r') as f:
        lines = [x.replace("\n", "") for x in f.readlines()]

        seeds = [int(x) for x in lines[0].removeprefix('seeds: ').strip().split(' ')]

        list_of_maps = []
        for line in lines[2:]:
            if line.endswith("map:"):
                list_of_maps.append([])
            elif line == "":
                continue
            else:
                list_of_maps[-1].append([int(x) for x in line.split(' ')])

        return seeds, list_of_maps

def map_seed(seed_nr, map_of_maps):
    nr = seed_nr
    for map in map_of_maps:
        for map_range in map:
            target_start, source_start, length = map_range
            if source_start <= nr <= source_start + length:
                nr = target_start + (nr - source_start)
                break
    return nr

seeds, map_of_maps = read_input()
for seed in seeds:
    print(map_seed(seed, map_of_maps))

ans = min(map_seed(x, map_of_maps) for x in seeds)

print(ans)
