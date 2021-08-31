# @Crate_Time  : 2021/8/31 21:15 
# @Author      : 孙北晨 
"""
    Introduction:
    
"""
# 6月7号改自main_csi_raw_9。数据只在程序运行时加载一次，提高了速度。
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm
import scipy.io as sio
import torchvision
from torch.utils.data import TensorDataset,DataLoader, ConcatDataset
import os
from sklearn.model_selection import train_test_split
import pandas as pd
import models
import utils
import re

# root_source = [r'D:\data\wiar3.0_CSI_little_example\exmaple10\1',
#                r'D:\data\wiar3.0_CSI_little_example\exmaple10\2',
#                r'D:\data\wiar3.0_CSI_little_example\exmaple10\3',
#                r'D:\data\wiar3.0_CSI_little_example\exmaple10\4',
#                r'D:\data\wiar3.0_CSI_little_example\exmaple10\5']
root_source = [r'data\example10\1',
               r'data\example10\2',
               r'data\example10\3',
               r'data\example10\4',
               r'data\example10\5']
BATCH_SIZE = 32
N_CLASS = 6
LEARNING_RATE = 0.003
MOMENTUM = 0.9
DECAY = 5e-3
EPOCH = 200
PRETRAINED = 1  # 是否预训练
EARLY_STOP = 1000
SPLIT_RATE = 0.7