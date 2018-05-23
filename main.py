# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:25:45 2018

@author: Martin
"""
import json

class reader:
    def __init__(self):
        self.blocks=[]
        self.traps=[]
        self.goals=[]
        
    def read(self,file):
        print("Read from file: ",file)
        file_content  = open(file).read()
        self.data = json.loads(file_content)
        self.x=self.data["width"]
        self.y=self.data["height"]
        self.cost=self.data["cost"]
        for b in self.data["block"]:
            self.blocks.append([self.data["block"][b]["x"],self.data["block"][b]["y"]])
        for t in self.data["trap"]:
            self.traps.append([self.data["trap"][t]["x"],self.data["trap"][t]["y"],self.data["trap"][t]["r"]])
        for g in self.data["goal"]:
            self.goals.append([self.data["goal"][g]["x"],self.data["goal"][g]["y"],self.data["goal"][g]["r"]])
        
    def getGridWorld(self):
        world = gridworld(self.x,self.y,self.blocks,self.traps,self.goals,self.cost)
        return world
        
class gridworld:
    def __init__(self,_x,_y,_block,_trap,_goal,_cost):
        self.x=_x
        self.y=_y
        self.block=_block
        self.trap =_trap
        self.goal =_goal
        self.cost =_cost
        self.arr = []
        for ay in range(self.y):
            tmp = []
            for ax in range(self.x):
                tmp.append(0)
            self.arr.append(tmp)
        for b in self.block:
            self.arr[b[1]][b[0]]="X"
        for t in self.trap:
            self.arr[t[1]][t[0]]=t[2]
        for g in self.goal:
            self.arr[g[1]][g[0]]=g[2]
        print("Created ",self.x,"x",self.y,"Gridworld\n")
        
    def printLine(self):
        print("+-----+",end="")
        for w in range(self.x-2):
            print("-----+",end="")
        print("-----+")
                    
    def printFieldArr(self,posY):
        print("|",end="")
        for elem in self.arr[posY]:
            print(str(elem).ljust(5),end="")
            print("|",end="")
        print(end="\n")
        
    def printWorld(self):
        i=0
        for h in range(self.y*2+1):
            if(h%2==1):
                self.printFieldArr(i)
                i+=1
            else:
                self.printLine()
    
    def printArray(self):
        print(self.arr)

"""world = gridworld(5,5,[[1,2],[2,2],[3,2]],[[4,1,-10]],[[4,0,1]])
world.printWorld()
world.printArray()"""
read=reader()
read.read("grid4x3.json")
world = read.getGridWorld()
world.printWorld()
world.printArray()
