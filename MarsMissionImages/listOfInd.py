#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:33:28 2019

@author: yelena
"""
import numpy as np


def listOfInd(m,px):
    mi = np.floor(m/px)
    if mi%2==0:
        #start from center
        istart = round(m/2)
        arr = np.arange(mi/2)
        ind = np.concatenate([istart - px*(arr+1),istart + px*arr])
        ind.sort()
    else:
        istart = round(m/2)-px/2
        arr = np.arange(mi/2)
        ind = np.concatenate([istart - px*(arr[1:]), istart +px*arr])
        ind.sort()
    return ind