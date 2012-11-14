import country
import DipConts

class World(object):

	def __init__(self, users = [ player1, player2, player3, player4, player5, player6, player7], nations = DipConts.Countries, locs = DipConts.Locations, supcents = DipConts.SupplyCenters, adjLocs = DipConts.AdjacentLocations):
		self.countries = []

		for i in range(countries):
			self.countries.append( country.Country( nations[i]["Locations"], nations[i]["SupplyCenters"], nations[i]["Name"], users[i]))
		self.locs = locs
		self.supcents = supcents
		self.adjLocs = adjLocs

	def update(self, actions):
		pass

	def conflicts (self):
		pass

	def moves (self):
		pass

	def convoys (self):
		pass
	
	def attacks (self):
		pass

	def supports (self):
		pass

	def reset_troops (self):
		pass



		


