# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:24:01 2021

@author: BENH VIEN CONG NGHE
"""
import numpy as np
a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
	
print("mean a = ", np.mean(a, dtype=np.float64))