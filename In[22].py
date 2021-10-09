# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:46:16 2021

@author: BENH VIEN CONG NGHE
"""
import numpy as np
np.random.randint(0, 2)
coins = np.random.randint(2, size=1000) 
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)