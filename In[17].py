# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:39:15 2021

@author: BENH VIEN CONG NGHE
"""

import numpy as np
scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])
 
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='lower'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='higher'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='linear'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='nearest'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='midpoint'))
