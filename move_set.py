moves_dict = {}
for i in range(len(locations)):
	moves_dict[locations[i]] = [actions[i],dests[i],second[i]]


for loc in moves_dict:
	if moves_dict[loc][0] == 'attack':
		country.move(loc,loc[1],world)
	if moves_dict[loc][0] == 'convoy':
		country.convoy(loc,loc[1],loc[2],world)
	if moves_dict[loc][0] == 'support':
		country.support(loc,loc[1],loc[2],world)
		
world.turn()
		
