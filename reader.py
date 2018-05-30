import json
from gridworld import gridworld

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