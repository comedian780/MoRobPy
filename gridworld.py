# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:18:10 2018

@author: Martin
"""
import numpy as np
from printer import printer

class gridworld:
    def __init__(self,_x,_y,_block,_trap,_goal,_cost,_gamma,_prob_succ):
        self.x=_x
        self.y=_y
        self.block=_block
        self.trap =_trap
        self.goal =_goal
        self.cost =_cost
        self.arr = [[0 for x in range(_x)]for y in range(_y)]
        self.rewardArr = [[0 for x in range(_x)]for y in range(_y)]
        self.ArrowArr = [[0 for x in range(_x)]for y in range(_y)]
        self.gamma = _gamma
        self.prob_succ = _prob_succ
        self.prob_fail = (1-self.prob_succ)/2
        self.printer = printer()
        self.iter=0

        for b in self.block:
            self.arr[b[1]][b[0]]='X'
            self.ArrowArr[b[1]][b[0]]='X'
            self.rewardArr[b[1]][b[0]]='X'
        for t in self.trap:
            self.arr[t[1]][t[0]]=float(t[2])
            self.ArrowArr[t[1]][t[0]]=float(t[2])
            self.rewardArr[t[1]][t[0]]=float(t[2])
        for g in self.goal:
            self.arr[g[1]][g[0]]=float(g[2])
            self.ArrowArr[g[1]][g[0]]=float(g[2])
            self.rewardArr[g[1]][g[0]]=float(g[2])
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
        self.printer.printArray(self.rewardArr,5,2)
    
    def printArrow(self):
        self.printer.printArray(self.ArrowArr,5,2)
        
    def up(self,x,y):
        if(y==0 or self.rewardArr[y-1][x]=='X'):
            return self.rewardArr[y][x]
        else:
            return self.rewardArr[y-1][x]
        
    def left(self,x,y):
        if(x==0 or self.rewardArr[y][x-1]=='X'):
            return self.rewardArr[y][x]
        else:
            return self.rewardArr[y][x-1]
    
    def down(self,x,y):
        if(y==(self.y-1) or self.rewardArr[y+1][x]=='X'):
            return self.rewardArr[y][x]
        else:
            return self.rewardArr[y+1][x]
            
    def right(self,x,y):
        if(x==(self.x-1) or self.rewardArr[y][x+1]=='X'):
            return self.rewardArr[y][x]
        else:
            return self.rewardArr[y][x+1]
        
    def isFieldTrap(self,x,y):
        for i in range(0,len(self.trap)):
            if(self.trap[i][0]==x and self.trap[i][1]==y):
                return i
        return -1
    
    def isFieldGoal(self,x,y):
        for i in range(0,len(self.goal)):
            if(self.goal[i][0]==x and self.goal[i][1]==y):
                return i
        return -1
    
    def isSame(self,ar1,ar2):
        cnt=0
        for y in range(0,len(ar1)):
            for x in range(0,len(ar1[0])):
                #print(ar1,ar2)
                if(type(ar1[y][x])==type("")):
                    if(ar1[y][x]==ar2[y][x]):
                        cnt+=1
                else:
                    if(abs(ar1[y][x]-ar2[y][x])<0.00001):
                        cnt+=1
        #print(len(ar1)*len(ar1[0]))
        #print(cnt)
        if(cnt==len(ar1)*len(ar1[0])):
            return 1
        else:
            return 0
        
    def calcVIStep(self):
        rewardNew = []
        rewardNew = self.rewardArr
        for y in range(len(self.rewardArr)):
            for x in range(len(self.rewardArr[y])):
                rew=[0,0,0,0]
                isTrap=self.isFieldTrap(x,y)
                isGoal=self.isFieldGoal(x,y)
                """if(self.oldrewardArr[y][x]=='X'):
                    print("Block")
                elif(isTrap>=0):
                    print("Trap")
                elif(isGoal>=0):
                    print("Goal")
                else:"""
                if( self.rewardArr[y][x]!='X' and isTrap<0 and isGoal<0):
                    """print(self.up(x,y))
                    print(self.left(x,y))
                    print(self.down(x,y))
                    print(self.right(x,y))"""
                    rew[0]=(self.prob_succ*self.up(x,y)+self.prob_fail*self.left(x,y)+self.prob_fail*self.right(x,y))
                    rew[1]=(self.prob_succ*self.left(x,y)+self.prob_fail*self.down(x,y)+self.prob_fail*self.up(x,y))
                    rew[2]=(self.prob_succ*self.down(x,y)+self.prob_fail*self.right(x,y)+self.prob_fail*self.left(x,y))
                    rew[3]=(self.prob_succ*self.right(x,y)+self.prob_fail*self.up(x,y)+self.prob_fail*self.down(x,y))
                    #print(self.cost + self.gamma * max(rew))
                    rewardNew[y][x] = self.cost + self.gamma * max(rew)
                    #print("Max:",max(rew))
                    direction = rew.index(max(rew))
                    #print("Direction:",direction)
                    if(direction==0):
                        self.ArrowArr[y][x]="up"
                    elif(direction==1):
                        self.ArrowArr[y][x]="left"
                    elif(direction==2):
                        self.ArrowArr[y][x]="down"
                    elif(direction==3):
                        self.ArrowArr[y][x]="right"
        self.rewardArr=rewardNew
        if(self.iter>1):
            if(self.isSame(self.rewardArr,rewardNew)):
               self.konv=1
        self.iter+=1
        
    def calcVI(self):
        self.konv = 0
        while(self.konv==0):
            self.calcVIStep()
            print("\nIteration",self.iter)
            self.printState() 

    def printArray(self):
        print(self.arr)
