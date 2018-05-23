# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:25:45 2018

@author: Martin
"""

"""gridworld = ["+---+---+---+---+---+",
             "|   |   |   |   | +1|",
             "+---+---+---+---+---+",
             "|   | X |   |   | -1|",
             "+---+---+---+---+---+",
             "|   |   |   |   |   |",
             "+---+---+---+---+---+",
             "|   |   |   |   |   |",
             "+---+---+---+---+---+"]"""

class gridworld:
    def __init__(self,_x,_y,_block,_trap,_goal):
        self.x=_x
        self.y=_y
        self.block=_block
        self.trap =_trap
        self.goal =_goal
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
        
    def printLine(self):
        print("+-----+",end="")
        for w in range(self.x-2):
            print("-----+",end="")
        print("-----+")
    
    def printField(self,posY):
        if(posY==1):
            posY=0
        else:
            posY=posY-2
        for w in range(self.x):
            if((self.block[0][0]==w) and (self.block[0][1]==posY)):
                if(w==0):
                    print("|  X  |",end="")
                elif(w==self.x-1):
                    print("  X  |",end="\n")
                else:
                    print("  X  |",end="")
            elif((self.trap[0][0]==w) and (self.trap[0][1]==posY)):
                if(w==0):
                    print("| ",str(self.trap[0][2]),"|",end="")
                elif(w==self.x-1):
                    print(" ",str(self.trap[0][2]),"|",end="\n")
                else:
                    print(" ",str(self.trap[0][2]),"|",end="")
            elif((self.goal[0][0]==w) and (self.goal[0][1]==posY)):
                if(w==0):
                    print("| ",str(self.goal[0][2]),"|",end="")
                elif(w==self.x-1):
                    print(" ",str(self.goal[0][2])," |",end="\n")
                else:
                    print(" ",str(self.goal[0][2])," |",end="")
            else:
                if(w==0):
                    print("|     |",end="")
                elif(w==self.x-1):
                    print("     |",end="\n")
                else:
                    print("     |",end="")
        
    def printWorld(self):
        for h in range(self.y*2+1):
            if(h%2==1):
                self.printField(h)
            else:
                self.printLine()
    
    def printArray(self):
        print(self.arr)

world = gridworld(5,5,[[1,2],[2,2],[3,2]],[[3,1,-1]],[[3,0,1]])
world.printWorld()
world.printArray()   
    
"""for elem in gridworld:
    print(elem);"""