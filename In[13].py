# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:34:51 2021

@author: BENH VIEN CONG NGHE
"""

import numpy as np
a = np.array([1, np.nan, 3, 4])
print("var = ", np.var(a))
print("std = ", np.std(a))
print("nanvar = ", np.nanvar(a))
print("nanstd = ", np.nanstd(a))