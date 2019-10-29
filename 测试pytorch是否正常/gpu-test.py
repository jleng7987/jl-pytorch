# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:48:36 2019

@author: SIA-JL
"""

import torch
flag = torch.cuda.is_available()
print(flag)

x = torch.Tensor(5, 3)
print(x)

