
input_list = [x[:-1] for x in open("input.txt", "r").readlines()]

points = 0
for card in input_list:
    winning_nums = [int(i) for i in card.split(':')[1].split('|')[0].split(' ') if i.isdigit()]
    your_nums = [int(i) for i in card.split(':')[1].split('|')[1].split(' ') if i.isdigit()]

    winners = 0
    for your_num in your_nums:
        winners += 1 if your_num in winning_nums else 0

    points += 2**(winners-1) if winners > 0 else 0

print(points)
