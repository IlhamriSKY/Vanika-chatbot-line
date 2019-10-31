# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class prog:
    def split(arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr   = arr[size:]
        arrs.append(arr)
        return arrs

    def _parseCurrency(cash):
        return cash.split(',')[0].replace('.',"")

    def formatrupiah(uang):
        y = str(uang)
        if len(y) <= 3 :
            return 'Rp. ' + y
        else :
            p = y[-3:]
            q = y[:-3]
            return prog.formatrupiah(q) + '.' + p