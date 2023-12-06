

def read_input():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        times = lines[0]
        distances = lines[1]

        times = [int(x) for x in times.split(":")[1].strip().split(" ") if x != ""]
        distances = [int(x) for x in distances.split(":")[1].strip().split(" ") if x != ""]

        return times, distances

def solve(time, distance):

    ans = 0
    for x in range(0, time):
        speed = x
        remaining_time = time - x
        distance_covered = speed * remaining_time
        if distance_covered > distance:
            ans += 1
    return ans
times, distances = read_input()

print(times, distances)

answers = [solve(x, y) for x, y in zip(times, distances)]

print(answers)

# multipling all the answers together
ans = 1
for x in answers:
    ans *= x
print(ans)
