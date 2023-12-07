from functools import cmp_to_key


def read_input():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]

        return [(x.split(" ")[0], int(x.split(" ")[1])) for x in lines]


def get_rank(poker_hand):
    # if it has five of a kind
    if len(set(poker_hand)) == 1:
        return 10
    # if it has four of a kind
    if len(set(poker_hand)) == 2 and any(poker_hand.count(x) == 4 for x in set(poker_hand)):
        return 9
    # if it has a full house
    if len(set(poker_hand)) == 2 and any(poker_hand.count(x) == 3 for x in set(poker_hand)) and any(
            poker_hand.count(x) == 2 for x in set(poker_hand)):
        return 8
    # if it has three of a kind
    if any(poker_hand.count(x) == 3 for x in set(poker_hand)):
        return 7
    # if it has two pairs
    if len(set(poker_hand)) == 3 and any(poker_hand.count(x) == 2 for x in set(poker_hand)):
        return 6
    # if it has one pair
    if len(set(poker_hand)) == 4 and any(poker_hand.count(x) == 2 for x in set(poker_hand)):
        return 5
    return 4


def get_card_value(card):
    card_value = card[0]
    if card_value == "A":
        return 14
    if card_value == "K":
        return 13
    if card_value == "Q":
        return 12
    if card_value == "J":
        return 11
    if card_value == "T":
        return 10
    return int(card_value)


def compare_hands(poker_hand1, poker_hand2):
    rank1 = get_rank(poker_hand1[0])
    rank2 = get_rank(poker_hand2[0])

    if rank1 > rank2:
        return 1
    if rank1 < rank2:
        return -1

    return compare_equal_rank(poker_hand1, poker_hand2)


def compare_equal_rank(poker_hand1, poker_hand2):
    # sort the poker hands, by A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
    # poker_hand1 = sorted(poker_hand1[0], key=lambda x: get_card_value(x), reverse=True)
    # poker_hand2 = sorted(poker_hand2[0], key=lambda x: get_card_value(x), reverse=True)
    #
    # print(poker_hand1)
    # print(poker_hand2)
    for (card1, card2) in zip(poker_hand1[0], poker_hand2[0]):
        # print(card1, card2)
        if get_card_value(card1) > get_card_value(card2):
            return 1
        if get_card_value(card1) < get_card_value(card2):
            return -1

    print("equal rank")
    return 0


data = read_input()

print(read_input())

sorted_hands = sorted(data, key=cmp_to_key(compare_hands), reverse=False)

print(sorted_hands)

# multiply each hand by its position in the sorted list and sum it up
ans = sum([(x[0] + 1) * x[1][1] for x in enumerate(sorted_hands)])
# ans = sum([x[0] for x in enumerate(sorted_hands)])

print(ans)

# print(compare_hands(('KK677', 28), ('KTJJT', 220)))
