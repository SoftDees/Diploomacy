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
		
	def __str__(self):
		return "This is the glorious country of %s." %(self.name)
		
	def move(Loc, Dest):
		world.actions.append([Loc, 1, Dest, None])
	
	def hold(Loc):
		world.actions.append([Loc, 2, None, None])
	
	def support(Loc, Dest, Dest2):
		world.actions.append([Loc, 3, Dest, Dest2])
	
	def convoy(Loc, Dest, Dest2):
		world.actions.append([Loc, 4, Dest, Dest2])
	
	def addtroop(self, Loc):
		if Loc in self.locations:
			return 1
		elif length(self.locations) >= length(self.supply):
			return 2
		else:
			self.locations.append(Loc)
			return 0
	
	def subtroop(self, Loc):
		if Loc not in self.locations:
			return 1
		else: 
			ind = self.locations.index(Loc)
			check = self.locations.pop(ind)
			return 0
			
	def movetroop(self, Loc, Dest):
		if Loc not in self.locations:
			return 1
		else:
			ind = self.locations.index(Loc)
			check = self.locations.pop(ind)
			self.locations.append(Dest)
			return 0
		
