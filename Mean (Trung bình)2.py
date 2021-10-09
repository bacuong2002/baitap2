# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:17:45 2021

@author: BENH VIEN CONG NGHE
"""
import numpy as np
X = np.array([[1, 2], [3, 4]])
print("Mean X = ", np.mean(X))
print("Mean X với axis = 0: ", np.mean(X, axis=0))
print("Mean X với axis = 1: ", np.mean(X, axis=1))