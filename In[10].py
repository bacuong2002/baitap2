# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:30:41 2021

@author: BENH VIEN CONG NGHE
"""

import numpy as np
x = np.array([2, np.nan, 5, 9])
print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))