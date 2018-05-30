# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:18:10 2018

@author: Martin
"""
import numpy as np
from printer import printer

class gridworld:
    def __init__(self,_x,_y,_block,_trap,_goal,_cost):
        self.x=_x
        self.y=_y
        self.block=_block
        self.trap =_trap
        self.goal =_goal
        self.cost =_cost
        self.arr = [[0 for x in range(_x)]for y in range(_y)]
        self.rewArr = [[0 for x in range(_x)]for y in range(_y)]
        self.ArrowArr = [[0 for x in range(_x)]for y in range(_y)]
        self.gamma = 0.9
        self.prob_succ = 0.8
        self.prob_fail = (1-self.prob_succ)/2
        self.printer = printer()
        self.iter=0

        for b in self.block:
            self.arr[b[1]][b[0]]='X'
            self.ArrowArr[b[1]][b[0]]='X'
            self.rewArr[b[1]][b[0]]='X'
        for t in self.trap:
            self.arr[t[1]][t[0]]=float(t[2])
            self.ArrowArr[t[1]][t[0]]=float(t[2])
            self.rewArr[t[1]][t[0]]=float(t[2])
        for g in self.goal:
            self.arr[g[1]][g[0]]=float(g[2])
            self.ArrowArr[g[1]][g[0]]=float(g[2])
            self.rewArr[g[1]][g[0]]=float(g[2])
        print("Created ",self.x,"x",self.y,"Gridworld")
        print("With",len(self.trap),"Traps and",len(self.goal),"Goals")
        
    def printInfo(self):
        print(self.x,"x",self.y,"Gridworld")
        print("With",len(self.trap),"Traps and",len(self.goal),"Goals")
        self.printWorld()
        
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
        self.printer.printArray(self.arr,5,1)
        
    def printState(self):
        self.printer.printArray(self.rewArr,5,2)
    
    def printArrow(self):
        self.printer.printArray(self.ArrowArr,5,2)
        
    def up(self,x,y):
        if(y==0 or self.oldRewArr[y-1][x]=='X'):
            return 0
        else:
            return self.oldRewArr[y-1][x]
        
    def left(self,x,y):
        if(x==0 or self.oldRewArr[y][x-1]=='X'):
            return 0
        else:
            return self.oldRewArr[y][x-1]
    
    def down(self,x,y):
        if(y==(len(self.oldRewArr)-1) or self.oldRewArr[y+1][x]=='X'):
            return 0
        else:
            return self.oldRewArr[y+1][x]
            
    def right(self,x,y):
        if(x==(len(self.oldRewArr)-1) or self.oldRewArr[y][x+1]=='X'):
            return 0
        else:
            return self.oldRewArr[y][x+1]
        
    def isFieldTrap(self,x,y):
        for i in range(0,len(self.trap)):
            if(self.trap[i][0]==x and self.trap[i][1]):
                return i
        return -1
    
    def isFieldGoal(self,x,y):
        for i in range(0,len(self.goal)):
            if(self.goal[i][0]==x and self.goal[i][1]):
                return i
        return -1
    
    def isSame(self,ar1,ar2):
        cnt=0
        for y in range(0,len(ar1)):
            for x in range(0,len(ar1[0])):
                print(ar1,ar2)
                if(type(ar1[y][x])==type("")):
                    if(ar1[y][x]==ar2[y][x]):
                        cnt+=1
                else:
                    if(abs(ar1[y][x]-ar2[y][x])<0.0001):
                        cnt+=1
        print(len(ar1)*len(ar1[0]))
        print(cnt)
        if(cnt==len(ar1)*len(ar1[0])):
            return 1
        else:
            return 0
        
    def calcVIStep(self):
        self.oldRewArr = self.rewArr
        for y in range(0,len(self.oldRewArr)):
            for x in range(0,len(self.oldRewArr[0])):
                rew=[]
                isTrap=self.isFieldTrap(x,y)
                isGoal=self.isFieldGoal(x,y)
                """if(self.oldRewArr[y][x]=='X'):
                    print("Block")
                elif(isTrap>=0):
                    print("Trap")
                elif(isGoal>=0):
                    print("Goal")
                else:"""
                if( self.oldRewArr[y][x]!='X' and isTrap<0 and isGoal<0):
                    """print(self.up(x,y))
                    print(self.left(x,y))
                    print(self.down(x,y))
                    print(self.right(x,y))"""
                    rew.append(self.prob_succ*self.up(x,y)+self.prob_fail*self.left(x,y)+self.prob_fail*self.right(x,y))
                    rew.append(self.prob_succ*self.left(x,y)+self.prob_fail*self.down(x,y)+self.prob_fail*self.up(x,y))
                    rew.append(self.prob_succ*self.down(x,y)+self.prob_fail*self.right(x,y)+self.prob_fail*self.left(x,y))
                    rew.append(self.prob_succ*self.right(x,y)+self.prob_fail*self.up(x,y)+self.prob_fail*self.down(x,y))
                    self.rewArr[y][x] = self.cost + self.gamma * max(rew)
                    direction = rew.index(max(rew))
                    if(direction==0):
                        self.ArrowArr[y][x]="up"
                    elif(direction==1):
                        self.ArrowArr[y][x]="left"
                    elif(direction==2):
                        self.ArrowArr[y][x]="down"
                    elif(direction==3):
                        self.ArrowArr[y][x]="right"
        if(self.iter>10):
            if(self.isSame(self.rewArr,self.oldRewArr)):
               self.konv=1
        self.iter+=1
        
    def calcVI(self):
        self.konv = 0
        while(self.konv==0):
            self.calcVIStep()
            print("\n",self.iter)
            self.printState() 

    def printArray(self):
        print(self.arr)
