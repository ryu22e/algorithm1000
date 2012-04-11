#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
"""
「石取りゲーム2」（「C言語による最新アルゴリズム事典」6ページより）
"""


def get_num(message):
    sys.stdout.write(message)
    n = ''
    while (not n.isdigit()):
        n = raw_input()
    return int(n)

# フィボナッチ数列
# リスト内包表記でやろうと思ったけど挫折。
# ぐぐってみるとやっている人がいた。
# http://d.hatena.ne.jp/sinsoku/20100901/1283351263
f = [1, 1]
for i in range(2, 21):
    f.append(f[i - 1] + f[i - 2])

n = get_num(u"石の数(2..100000)？")
if (not(2 <= n <= 100000)):
    sys.exit(1)
max_x = n - 1
my_turn = True
while(n != 0):
    print("%d 個まで取れます." % max_x)
    if (my_turn):
        x = n
        i = 20
        while(x != f[i]):
            if (f[i] < x):
                x -= f[i]
            i -= 1
        if (max_x < x):
            x = 1
        print(u"私は %d 個の石を取ります." % x)
    else:
        r = False
        while (not r or x < 1 or max_x < x):
            x = get_num(u"何個取りますか？")
            r = True
    n -= x
    max_x = 2 * x
    if (n < max_x):
        max_x = n
    print(u"残りは %d 個です." % n)
    my_turn = not my_turn

if (my_turn):
    print(u"あなたの勝ちです！")
else:
    print(u"私の勝ちです！")
