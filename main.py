# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:25:45 2018

@author: Martin
"""
from reader import reader

if __name__ == "__main__":
    read=reader()
    read.read("grid4x3.json")
    world =read.getGridWorld()
    world.printWorld()
    world.calcVI()
    print("\nResults:")
    world.printInfo()
    world.printArrow()
