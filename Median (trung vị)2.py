# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:27:07 2021

@author: BENH VIEN CONG NGHE
"""
import numpy as np
arr = np.array([[7, 4, 2], [3, 9, 5]])
print("median arr (axis = 0) = ", np.median(arr, axis=0))
print("median arr (axis = 1) = ", np.median(arr, axis=1))