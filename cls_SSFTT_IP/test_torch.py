# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:03:20 2022

@author: ZGR
"""

import torch
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())
print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.device_count())


