# -*- coding: UTF-8 -*-
from random import randint

name = input("请输入你的名字")

f = open('game.txt')
lines = f.readlines()
f.close()

scores = {}

for line in lines:
    s = line.split()
    scores[s[0]] = s[1:]
score = scores.get(name)

if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

print('你已经玩了%d次,最少%d轮猜出答案,平均%.2f轮猜出答案' % (game_times,
                                                                                  min_times,
                                                                                  avg_times))

num = randint(1, 100)
print('Guess what I think?')
bingo = False

current_times = 0

while bingo == False:
    answer = eval(input())
    current_times = current_times + 1
    if answer < num:
        print('too small!')
    elif answer > num:
        print('too big!')
    else:
        print('BINGO!')
        bingo = True

if min_times is 0 or current_times < min_times:
    min_times = current_times

game_times = game_times + 1

total_times = total_times + current_times

score[0] = str(game_times)
score[1] = str(min_times)
score[2] = str(total_times)

scores.update({name: score})

result = ' '
for key in scores:
    result += key + ' ' + ' '.join(scores[key]) + '\n'

f = open('game.txt', 'w')
f.write(result)
f.close()
