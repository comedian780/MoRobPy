# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:16:57 2018

@author: Martin
"""

class printer:
    def printLine(self,width,length):
        print("+"+str("").center(length,"-")+"+",end="")
        for w in range(width-2):
            print(str("").center(length,"-")+"+",end="")
        print(str("").center(length,"-")+"+")
        
    def printField(self,arr,y,length,acc):
        print("|",end="")
        for elem in arr[y]:
            if(type(elem)==type('X')):
                print(str(elem).center(length),end="")
            else:
                print(str(format(elem,".2f")).center(length),end="")
            print("|",end="")
        print(end="\n")
        
    def printArray(self,array,length,acc):
        i=0
        for h in range(len(array)*2+1):
            if(h%2==1):
                self.printField(array,i,length,acc)
                i+=1
            else:
                self.printLine(len(array[0]),length)