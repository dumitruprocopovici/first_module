# def score_hand(cards):
#     sum = 0
#     Aces = 0
#     for i in cards:
#         if i in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
#             sum += int(i)
#         elif i in ('J', 'Q', 'K'):
#             sum += 10
#         elif i == 'A':
#             Aces += 1
#             sum += 11
#     for i in range(Aces):
#         if sum > 21:
#             sum -= 10
#     return sum


def score_hand(cards):
    s = sum(c == 'A' or c.isdigit() and int(c) or 10 for c in cards)
    n = cards.count('A')
    return s + 10 * (n and s < 12)


print(score_hand(['A', 'A', 'A', 'A']))
