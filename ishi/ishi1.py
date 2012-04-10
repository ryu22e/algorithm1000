#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
"""
「石取りゲーム1」（「C言語による最新アルゴリズム事典」6ページより）
"""


def get_num(message):
    sys.stdout.write(message)
    n = ''
    while (not n.isdigit()):
        n = raw_input()
    return int(n)

n = get_num(u"石の数？")
m = get_num(u"1回に取れる最大の石の数？")
if (n < 1 or m < 1):
    sys.exit(1)
my_turn = True
while(n != 0):
    if (my_turn):
        x = (n - 1) % (m + 1)
        if (x == 0):
            x = 1
        print(u"私は%d個の石を取ります." % x)
    else:
        r = False
        while (not r or x <= 0 or m < x or n < x):
            x = get_num(u"何個取りますか？")
            r = True
    n -= x
    print(u"石の残り: %d個" % n)
    my_turn = not my_turn

if (my_turn):
    print(u"あなたの負けです！")
else:
    print(u"私の負けです！")
