from world_functions import *
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

	def __init__(self, Locations, supply, Name, usrname, color):
		
		self.locations = Locations
		self.supply = supply
		self.Name = Name
		self.usrname = usrname
		self.actions = []
		self.original = supply
		self.color = color
		
	def __str__(self):
		return "This is the glorious country of %s." %(self.name)
		
	def hold(self,Loc):
		self.actions.append([Loc,'attack', Loc, 1, None, self])	
		
	def move(self,Loc, Dest, world):
		
		if self.locations[Loc] == 'A':
			if Dest in world.locations[Loc]:
				self.actions.append([Loc, 'attack', Dest,1, None, self])
				return 0
			else:
				return 1
		elif self.locations[Loc] == 'F':
			if Dest in world.water[Loc]:
				self.actions.append([Loc, 'attack', Dest, 1, None, self])
				return 0
			else:
				return 1
		else:
			return 2
	
	def support(self,Loc, attacked, attacking, world):
		if self.locations[Loc] == 'A':
			if attacking in world.locations[Loc] and attacked in world.locations[attacking]:
				self.actions.append([Loc, 'support', attacked,1, attacking,self])
				return 0
			else:
				return 1
		elif self.locations[Loc] == 'F':
			if attacking in world.water[Loc] and attacked in world.water[attacking]:
				self.actions.append([Loc, 'support', attacked,1, attacking,self])
				return 0
			else:
				return 1
	
	def convoy(self,Loc, Dest, convoying, world):
		if convoying in world.water[Loc] and Dest in world.water[Loc]:
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
			if Loc in world.locations:
				self.locations[Loc] = 'A'
				return 0
			elif Loc in world.water:
				self.locations[Loc] = 'F'
				return 0
	
	def subtroop(self, Loc):	#Method for removing troops
		if Loc not in self.locations:
			return 1
		else: 
			check = self.locations.pop(Loc)
			return 0
			
	def movetroop(self, Loc, Dest): #Method for moving troops
		if Loc not in self.locations:
			return 1
		else:
			type_mil = self.locations[Loc]
			check = self.locations.pop(Loc)
			self.locations[Loc] = type_mil
			return 0
			
	def get_actions(self):
		#Add hold command for all locations without orders
		for locate in self.locations:
			hold = False
			for act in self.actions:
				if act[0] == locate:
					hold = True
			if hold == False:
				self.hold(locate)
				
		act_list = self.actions
		self.actions = []
		return act_list
		
		
	def update(self, actions, incomplete, world):
		for action in actions:
			if action[5] == self:
				check = self.movetroop(action[0], action[2])
				if not check == 0:
					error = True
		for action in incomplete:
			if action[5] == self:
				self.subtroop(action[0])
				#flag for user input OR remove troop
			
		world.update_supply()	
				
		if world.fall:
			if len(self.supply) > len(self.locations):
				#message to user for adding troops or add troops at random supply center
				viable = []
				for supply in self.supply:
					if supply not in self.locations and supply in self.original:
						viable.append(supply)
				
				if not viable == []:
					self.addtroop(random.choice(viable))
					
			elif len(self.supply) < len(self.locations):
				#message to user for subtracting troops or remove random army
				self.subtroop(random.choice(self.locations))			
				
if __name__ == "__main__":
	
	
	c1 = Country([1,3,5], [2,3], "Player 1", "p123")
	c2 = Country([7], [7, 10], "Player 2", "p1234")
	c3 = Country([6,8,9], [8,9], "Player 3", "p12345")
	w1 = world([c1,c2,c3])
	
	def test_1(world): #success
		world.countries[0].move(1,7,w1)
		world.countries[0].support(3,7,1,w1)
		world.countries[1].move(7,1,w1)
	
	def test_2(world): #success
		world.countries[0].move(1,3,w1)
		world.countries[0].move(3,5,w1)
		world.countries[0].move(5,7,w1)
		world.countries[2].support(6,7,5,w1)
		world.countries[1].hold(7)
		
	def test_3(world): #success
		world.countries[0].move(1,3,w1)
		world.countries[0].move(3,4,w1)
		
	def test_4(world):
		
		apple = 0
	
	test_2(w1)
	w1.turn()
	w1.turn()
	
	for country in w1.countries:
		print country.locations
		print country.supply
		print 
	
	
	
	
	"""c1 = Country([1,3,5], [2,3], "Player 1", "p123")
	c2 = Country([7], [7, 10], "Player 2", "p1234")
	print c1.addtroop(4)
	print c1.movetroop(5,5)
	print c2.addtroop(10)
	actlist = [[1,"attack",2, 1, None, c1]]
	c1.update(actlist,[])
	c2.update(actlist,[])
	print c1.locations
	print c2.locations"""
	
	
