#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


def exe1_a(a, b, c, s):
    @always_comb
    def comb():
        pass

    return instances()


def exe2(l, m, h, l_vd, l_am, l_vm, l_az, l_lj):
    @always_comb
    def comb():
        pass

    return instances()


def exe3(i3, i2, i1, i0, p1, p0, v):
    @always_comb
    def comb():
        pass

    return instances()


def exe4_simulando(a, b, c, d, e, f, g, h, i, j, k, l):
    @always_comb
    def comb():
        a.next = 1
        b.next = 0
        c.next = 0
        d.next = 1
        e.next = 1
        f.next = 0
        g.next = 1
        h.next = 1
        i.next = 1
        j.next = 0
        k.next = 0

    return instances()


def exe4_half_sub(x, y, b, d):
    @always_comb
    def comb():
        b.next = not x and y
        d.next = (not x and y) or (x and not y)

    return instances()


def exe4_full_sub(x, y, z, b, d):
    @always_comb
    def comb():
        b.next = (not x and z) or (not x and y and not z) or (x and y and z)
        d.next = (not x and not y and z) or (not x and y and not z) or (x and not y and not z) or (x and y and z)

    return instances()


def exe4_sub3(v2, v1, v0, p2, p1, p0, q2, q1, q0):
    b0 = Signal(bool(0))
    b1 = Signal(bool(0))
    b2 = Signal(bool(0))

    half_sub0 = exe4_half_sub(v0, p0, b0, q0)
    full_sub1 = exe4_full_sub(v1, p1, b0, b1, q1)
    full_sub2 = exe4_full_sub(v2, p2, b1, b2, q2)
    
    return instances()
