# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:01:55 2017

@author: Tane Yoroshi
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values