import random
class Country(object):
    
	"""
    def __init__(self, name = "country", president = "leader", land = [1,2,3], economy = random.randint(0,1000), military = random.randint(0,1000), wellbeing = random.randint(0,1000) ):
        self.name = name
        self.president = president
        self.land = land
        self.economy = economy
        self.military = military
        self.wellbeing = wellbeing
        self.countryscore = (economy+military+wellbeing)


    def __str__(self):
        return "This is the glorious country of %s. Our hallowed leader is %s." % (self.name,self.president)
"""

	def __init__(self, Locations, supply, Name, usrname):
		
		self.locations = Locations
		self.supply = supply
		self.Name = Name
		self.usrname = usrname
		self.actions = []
		
	def __str__(self):
		return "This is the glorious country of %s." %(self.name)
		
	def move(self,Loc, Dest, world):
		if Dest in world.locations[Loc]:
			self.actions.append([Loc, 'attack', Dest,1, None, self])
			return 0
		else:
			return 1
	
	def support(self,Loc, attacked, attacking, world):
		if attacking in world.locations[Loc] and attacked in world.locations[attacking]:
			self.actions.append([Loc, 'support', attacked,1, attacking,self])
			return 0
		else:
			return 1
	
	def convoy(self,Loc, Dest, convoying, world):
		if convoying in world.locations[Loc] and Dest in world.locations[convoying]:
			self.actions.append([Loc, 'convoy', Dest,1, convoying, self])
			return 0
		else:
			return 1
	
	def addtroop(self, Loc): #Method for adding troops
		if Loc in self.locations: 
			return 1
		elif len(self.locations) >= len(self.supply):
			return 2
		else:
			self.locations.append(Loc)
			return 0
	
	def subtroop(self, Loc):	#Method for removing troops
		if Loc not in self.locations:
			return 1
		else: 
			ind = self.locations.index(Loc)
			check = self.locations.pop(ind)
			return 0
			
	def movetroop(self, Loc, Dest): #Method for moving troops
		if Loc not in self.locations:
			return 1
		else:
			ind = self.locations.index(Loc)
			check = self.locations.pop(ind)
			self.locations.append(Dest)
			return 0
			
	def get_actions(self):
		act_list = self.actions
		self.actions = []
		return act_list
		
	def update(self, actions, incomplete):
		for action in actions:
			if action[5] == self:
				check = self.movetroop(action[0], action[2])
				if not check == 0:
					error = True
		for action in incomplete:
			if action[5] == self:
				apple = 0
				#self.subtroop(action[0])
				#flag for user input OR remove troop
				
		
c1 = Country([1,3,5], [2,3], "Player 1", "p123")
c2 = Country([7], [7, 10], "Player 2", "p1234")
"""print c1.addtroop(4)
print c1.movetroop(5,5)
print c2.addtroop(10)"""
actlist = [[1,"attack",2, 1, None, c1]]
c1.update(actlist,[])
c2.update(actlist,[])
print c1.locations
print c2.locations
