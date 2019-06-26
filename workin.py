#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:57:56 2019

@author: trejimmy5562
"""

from tqdm import tqdm
#import time
import random

loadNames = ["Hacking Mainframe", "Wiring Bitcoin to Offshore Accounts", "Attacking Firewall with Bot Army", "Branching Private Key with Merge Request", "Creating Sentient AI to Overtake Human Race"]
numBar = random.randint(0,4)

def loadBar(x):
    colz = random.randint(90,130)
    while((x+1) > 0):
        y = random.randint(0,4)
        for i in tqdm(range(int(9e6)), ncols=colz, desc=loadNames[y]):
            pass
        x = x - 1
    print("\nMainframe: Hacked")
    print("Joe Prather: Sux Lol")

loadBar(numBar)

""""""