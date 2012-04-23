#!/usr/bin/env python
# -*- coding: utf-8 -*-
from types import GeneratorType


def count_isomers(max_atomic, max_group):
    n = 0
    size = [n] * max_group
    length = [n] * max_group
    count = [n] * (max_atomic + 1)
    for i in range(max_group):
        l = length[i] + 1
        if (max_atomic / 2 < l):
            break
        si = size[i] + 1
        if (max_atomic < si + l):
            continue
        for j in range(i + 1):
            sj = si + size[j]
            if (max_atomic < sj + l):
                continue
            for k in range(j + 1):
                sk = sj + size[k]
                if (max_atomic < sk + l):
                    continue
                n += 1
                if (max_group <= n):
                    raise AssertionError
                size[n] = sk
                length[n] = l
    if (l <= max_atomic / 2):
        raise AssertionError
    for i in range(n + 1):
        si = size[i]
        for j in range(i + 1):
            if (length[i] != length[j]):
                continue
            sj = si + size[j]
            if (max_atomic < sj):
                continue
            count[sj] += 1
            for k in range(j + 1):
                sk = sj + size[k] + 1
                if (max_atomic < sk):
                    continue
                for h in range(k + 1):
                    sh = sk + size[h]
                    if (sh <= max_atomic):
                        count[sh] += 1
    for i in range(1, max_atomic + 1):
        yield (i, count[i])

if __name__ == '__main__':
    result = count_isomers(17, 2558)
    assert(result is not None)
    assert(type(result) == GeneratorType)
    assert(result.next() == (1, 1))
    assert(result.next() == (2, 1))
    assert(result.next() == (3, 1))
    assert(result.next() == (4, 2))
    assert(result.next() == (5, 3))
    assert(result.next() == (6, 5))
    assert(result.next() == (7, 9))
    assert(result.next() == (8, 18))
    assert(result.next() == (9, 35))
    assert(result.next() == (10, 75))
    assert(result.next() == (11, 159))
    assert(result.next() == (12, 355))
    assert(result.next() == (13, 802))
    assert(result.next() == (14, 1858))
    assert(result.next() == (15, 4347))
    assert(result.next() == (16, 10359))
    assert(result.next() == (17, 24894))
