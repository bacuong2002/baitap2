# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:22:12 2021

@author: BENH VIEN CONG NGHE
"""

import numpy as np
 
a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
 
 
print("a.shape: ", a.shape)
print("mean a = ", np.mean(a))