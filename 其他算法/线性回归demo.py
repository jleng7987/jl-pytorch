# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:20:07 2019

@author: SIA-JL
"""

import torch


# 标量（0维张量）
bl = torch.rand(10)
print(bl.size())

# 向量（1维张量）
xl = torch.rand([1,2,3,4,5,6,7,8,9])
print(xl.size())
