

def read_input():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        instructions = lines[0]
        graph = lines[2:]
        new_graph = []
        for item in graph:
            start_node = item.split(" = ")[0]
            left_node = item.split(" = ")[1].split(", ")[0].replace("(", "")
            right_node = item.split(" = ")[1].split(", ")[1].replace(")", "")
            new_graph.append((start_node, left_node, right_node))
        return instructions, new_graph

def iterate_graph(graph, instructions):
    current_point = "AAA"
    exit_point = "ZZZ"

    iterations = 0
    while current_point != exit_point:
        print(current_point, iterations)
        if current_point == exit_point:
            return iterations
        current_index = iterations % len(instructions)
        current, next_left, next_right = [x for x in graph if x[0] == current_point ][0]
        if instructions[current_index] == "L":
            current_point = next_left
        else:
            current_point = next_right
        iterations += 1
    return iterations


instructions, graph = read_input()

print(instructions)

print(graph)

print(iterate_graph(graph, instructions))

