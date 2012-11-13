import country
import random

class World(object):

	def __init__(self, names = ["country1", "country2", "country3", "country4"], players = ["player1", "player2", "player3", "player4"], resources = random.randint(0,1000), lands = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] ):
		self.players = players
		self.resources = resources
		countries = []
		for i in range(len(players)):
			countries.append(country.Country( names[i], players[i], lands[i]))
		self.countries = countries
		self.lands = lands





	def __str__(self):
		return "Welcome to this wonderful world! In this world, are the following countries: \n %s \n %s \n %s \n %s" % tuple(self.countries)



	def findcountry(self, name):
		for country in self.countries:
			if country.name == name:
				return Country


#	def randomevents():
wo = World()
print wo