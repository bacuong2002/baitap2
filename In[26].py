# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:49:14 2021

@author: BENH VIEN CONG NGHE
"""

import numpy as np
np.random.binomial(20, 0.5, 10) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())
