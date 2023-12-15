


def read_input():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        numbers = [[int(x) for x in line.split(" ")] for line in lines]
        return numbers


def compute_diff(numbers):
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    return diffs
def solve(numbers):
    # compute diff between each adjacent element
    ans = numbers[-1]
    current_arr = numbers
    while not all(x == 0 for x in current_arr):
        current_arr = compute_diff(current_arr)
        ans += current_arr[-1]
        # print(current_arr)

    return ans


numbers_arr = read_input()

answer_sum = sum(solve(numbers) for numbers in numbers_arr)

print(answer_sum)
