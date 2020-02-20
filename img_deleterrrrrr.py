#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:29:51 2019

@author: trejimmy5562
"""

import os
"""
this deletes all jpgs that do not have an accompanying xml file dor help with a yolo image processing project i am working on
"""
path1 = "/PATH/STUFF/jsdbnafdbf"
os.chdir(path1)
for filename in os.listdir(path1):
    #print(filename)
    if filename.endswith(".jpg"):
        filename1 = filename[:-4]
        filename2 = filename1 + '.xml'
        #print(filename2)
        if os.path.exists(filename2):
            pass
        else:
            os.chdir(path1)
            os.remove(filename)
            
print("Success!")


