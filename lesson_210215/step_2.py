# player_wins = [random.randint(0, 1000) for _ in range(20)]
player_wins = [
    540, 167, 930, 874, 894, 310,
    229, 2, 298, 349, 331, 768, 160,
    902, 491, 39, 725, 7, 784, 998
]
# x1000 -> 20 000 -> 20 000 000
print(player_wins)

att_example = [(930, 874, 894), (874, 894, 310), (349, 331, 768)]
# 3 times > 300

att = []
# for nums in zip(player_wins, player_wins, player_wins):
for nums in zip(player_wins, player_wins[1:], player_wins[2:]):
    if min(nums) >= 300:
        att.append(tuple(nums))
assert att == att_example, 'wrong result'
# print(att)