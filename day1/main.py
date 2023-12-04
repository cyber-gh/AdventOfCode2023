

def solve():
    f = open("input.txt", "r")
    ans = 0
    for line in f.readlines():
        target = line[:-1]
        digits = [int(x) for x in target if x.isdigit()]
        nr = 10 * int(digits[0]) + int(digits[-1])
        print(target)
        print(nr)
        ans += nr

    print(ans)
    f.close()


solve()
