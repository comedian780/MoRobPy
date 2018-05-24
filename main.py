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
    
class printer:
    def printLine(self,width,length):
        print("+"+str("").center(length,"-")+"+",end="")
        for w in range(width-2):
            print(str("").center(length,"-")+"+",end="")
        print(str("").center(length,"-")+"+")
        
    def printField(self,arr,y,length):
        print("|",end="")
        for elem in arr[y]:
            print(str(elem).center(length),end="")
            print("|",end="")
        print(end="\n")
        
    def printArray(self,array,length):
        i=0
        for h in range(len(array)*2+1):
            if(h%2==1):
                self.printField(array,i,length)
                i+=1
            else:
                self.printLine(len(array[0]),length)
        
        
class gridworld:
    def __init__(self,_x,_y,_block,_trap,_goal,_cost):
        self.x=_x
        self.y=_y
        self.block=_block
        self.trap =_trap
        self.goal =_goal
        self.cost =_cost
        self.arr = []
        self.rewArr = self.arr
        self.gamma = 0.5
        self.prob_succ = 0.8
        self.prob_fail = (1-self.prob_succ)/2
        
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
        
    """def printLine(self):
        print("+-----+",end="")
        for w in range(self.x-2):
            print("-----+",end="")
        print("-----+")
                    
    def printFieldArr(self,posY):
        print("|",end="")
        for elem in self.arr[posY]:
            print(str(elem).ljust(5),end="")
            print("|",end="")
        print(end="\n")"""
        
    def printWorld(self):
        self.printer = printer()
        self.printer.printArray(self.arr,3)
        
    def up(self,x,y):
        if(y==0 or self.arr[y-1][x]=='X'):
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y-1][x]
        
    def left(self,x,y):
        if(x==0 or self.arr[y][x-1]=='X'):
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y][x-1]
    
    def down(self,x,y):
        if(y==(len(self.arr)-1) or self.arr[y+1][x]=='X'):
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y+1][x]
            
    def right(self,x,y):
        if(x==(len(self.arr)-1) or self.arr[y][x+1]=='X'):
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y][x+1]
        
    def calcVIStep(self):
        self.oldRewArr = self.rewArr
        rew = []
        for y in self.rewArr:
            for x in self.rewArr[0]:
                rew[0] = self.prob_succ*self.up(x,y)+self.prob_fail*self.left(x,y)+self.prob_fail*self.right(x,y)
                rew[1] = self.prob_succ*self.left(x,y)+self.prob_fail*self.down(x,y)+self.prob_fail*self.up(x,y)
                rew[2] = self.prob_succ*self.down(x,y)+self.prob_fail*self.right(x,y)+self.prob_fail*self.left(x,y)
                rew[3] = self.prob_succ*self.right(x,y)+self.prob_fail*self.up(x,y)+self.prob_fail*self.down(x,y)
                self.rewArr = self.cost + self.gamma+max(rew)
        
        
    """def printWorld(self):
        i=0
        for h in range(self.y*2+1):
            if(h%2==1):
                self.printFieldArr(i)
                i+=1
            else:
                self.printLine()"""
    
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
