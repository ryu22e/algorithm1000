#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
「安定な結婚の問題」（「C言語による最新アルゴリズム事典」4ページより）
"""


def marriage(girls_ranks, boys_ranks):
    pairs = {}
    positions = {}
    for boy in boys_ranks.keys():
        s = boy
        while (s is not None):
            print("-" * 30)
            position = positions.get(s, 0)
            positions[s] = position + 1
            girl = boys_ranks.get(s)[position]
            print(u"男%s「女%sさん、結婚してください！」" % (s, girl))
            girls_rank = girls_ranks.get(girl)
            # プロポーズした女性にとっての男性のランキングを調べる。
            proposed_boys_rank = girls_rank.index(s)
            # （既に婚約している場合は）婚約者のランキングを調べる。
            if (girl in pairs):
                fiancees_rank = girls_rank.index(pairs.get(girl))
            else:
                fiancees_rank = None
            if (fiancees_rank is None or proposed_boys_rank < fiancees_rank):
                # 女性が未婚なら、婚約成立になる。
                # 女性が既に婚約している場合は、プロポーズした男性が婚約者より上のランクであれば、前の婚約を破棄して婚約する。
                print(u"女%s「よろしくお願いします」" % girl)
                fiancee = pairs.get(girl)
                if (fiancee is not None):
                    print(u"女%s「男%sさん、婚約破棄してください」" % (girl, fiancee))
                    print(u"男%s「（´・ω・｀）」" % fiancee)
                pairs[girl], s = s, pairs.get(girl)
            else:
                print(u"女%s「ごめんなさい」" % girl)
            print("-" * 30)

    return tuple([(girl, boy) for girl, boy in pairs.items()])

if __name__ == '__main__':
    # 各女性の好み。
    girls_ranks = {
            '1': ['a', 'b', 'c', 'd'],
            '2': ['c', 'b', 'a', 'd'],
            '3': ['a', 'b', 'd', 'c'],
            '4': ['c', 'a', 'd', 'b'],
            }
    # 各男性の好み。
    boys_ranks = {
            'a': ['1', '2', '3', '4'],
            'b': ['2', '1', '4', '3'],
            'c': ['2', '3', '1', '4'],
            'd': ['1', '4', '3', '2'],
            }
    pairs = marriage(girls_ranks, boys_ranks)
    assert(pairs is not None)
    assert(len(pairs) == 4)
    assert(('1', 'a') in pairs)
    assert(('2', 'c') in pairs)
    assert(('3', 'b') in pairs)
    assert(('4', 'd') in pairs)
    print(u"--成立したカップル--")
    for pair in pairs:
        print(u"女%s: 男%s" % (pair[0], pair[1]))
