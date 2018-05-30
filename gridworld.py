# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:18:10 2018

@author: Martin
"""
from printer import printer

class gridworld:
    def __init__(self,_x,_y,_block,_trap,_goal,_cost):
        self.x=_x
        self.y=_y
        self.block=_block
        self.trap =_trap
        self.goal =_goal
        self.cost =_cost
        self.arr = []
        self.rewArr = []
        self.ArrowArr = []
        self.gamma = 0.5
        self.prob_succ = 0.8
        self.prob_fail = (1-self.prob_succ)/2
        self.printer = printer()
        
        for ay in range(self.y):
            tmp = []
            for ax in range(self.x):
                tmp.append(0.0)
            self.arr.append(tmp)
            self.rewArr.append(tmp)
            #self.ArrowArr.append(tmp)
        for b in self.block:
            self.arr[b[1]][b[0]]='X'
        for t in self.trap:
            self.arr[t[1]][t[0]]=float(t[2])
        for g in self.goal:
            self.arr[g[1]][g[0]]=float(g[2])
        print("Created ",self.x,"x",self.y,"Gridworld\n")
        print("With",len(self.trap),"Traps and",len(self.goal),"Goals")
        
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
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y-1][x]
        
    def left(self,x,y):
        if(x==0 or self.oldRewArr[y][x-1]=='X'):
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y][x-1]
    
    def down(self,x,y):
        if(y==(len(self.oldRewArr)-1) or self.oldRewArr[y+1][x]=='X'):
            return self.oldRewArr[y][x]
        else:
            return self.oldRewArr[y+1][x]
            
    def right(self,x,y):
        if(x==(len(self.oldRewArr)-1) or self.oldRewArr[y][x+1]=='X'):
            return self.oldRewArr[y][x]
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
    
    def calcVIStep(self):
        self.oldRewArr = self.rewArr
        for y in range(0,len(self.oldRewArr)):
            for x in range(0,len(self.oldRewArr[0])):
                rew=[]
                print("Position: ("+str(x)+"|"+str(y)+") Inhalt:",self.oldRewArr[y][x])
                isTrap=self.isFieldTrap(x,y)
                isGoal=self.isFieldGoal(x,y)
                if(self.oldRewArr[y][x]=='X'):
                    print("Block")
                elif(isTrap>=0):
                    print("Trap")
                elif(isGoal>=0):
                    print("Goal")
                else:
                    print(self.up(x,y))
                    print(self.left(x,y))
                    print(self.down(x,y))
                    print(self.right(x,y))
                    rew.append(self.prob_succ*self.up(x,y)+self.prob_fail*self.left(x,y)+self.prob_fail*self.right(x,y))
                    rew.append(self.prob_succ*self.left(x,y)+self.prob_fail*self.down(x,y)+self.prob_fail*self.up(x,y))
                    rew.append(self.prob_succ*self.down(x,y)+self.prob_fail*self.right(x,y)+self.prob_fail*self.left(x,y))
                    rew.append(self.prob_succ*self.right(x,y)+self.prob_fail*self.up(x,y)+self.prob_fail*self.down(x,y))
                    self.rewArr[y][x] = self.cost + self.gamma * max(rew)
                    direction = rew.index(max(rew))
                    #self.ArrowArr.append(direction)
                    if(direction==0):
                        self.ArrowArr[y][x]="up"
                    elif(direction==1):
                        self.ArrowArr[y][x]="left"
                    elif(direction==2):
                        self.ArrowArr[y][x]="down"
                    elif(direction==3):
                        self.ArrowArr[y][x]="right"
        
    def calcVI(self):
        notKonv = 1
        while(notKonv<50):
            self.calcVIStep()
            self.printState()
            notKonv+=1  

    def printArray(self):
        print(self.arr)
