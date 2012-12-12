class world (object):
	
	def __init__ (self, countries):
		self.countries = countries
		"""self.locations = {1:[1,2,3,4,5,6,7,8,9,10],2:[1,2,3,4,5,6,7,8,9,10],3:[1,2,3,4,5,6,7,8,9,10],4:[1,2,3,4,5,6,7,8,9,10],5:[1,2,3,4,5,6,7,8,9,10],6:[1,2,3,4,5,6,7,8,9,10],7:[1,2,3,4,5,6,7,8,9,10],8:[1,2,3,4,5,6,7,8,9,10],9:[1,2,3,4,5,6,7,8,9,10],10:[1,2,3,4,5,6,7,8,9,10]}"""
		self.locations = {
			'BAB': ['TRM','FAC','VMO','MCR','CHL','STR'],
			'CHL':['BAB','MCR','CAC','LAS','OMM','STR','ROD'],
			'MCR':['VMO','CAC','CHL','BAB'],
			'CAC':['MCR','CHL','LPB','MAC','ROD'],
			'LAS':['CHL','PML','MSO','ROD'],
			'MSO':['LAS','OMM','FLG','PML'],
			'OMM':['CHL','STR','DIH','MSO'],
			'TRM':['BAB','LDK','FAC','BAS'],
			'FAC':['LDK','TRM','BAB','STR','ADM'], 
			'WHE':['WHN','WHW','TTT','EHW','EWF'],
			'TTT':['MED','WHN','WHE','EHW','EHN'],
			'BAS':['TRM','LDK','SLR','NLB','LBO','ADM','WWS'],
			'SLR':['BAS','NLB','DSC'],
			'DSC':['SLR','NLB','BBQ','NWH','WWS'],
			'NLB':['SLR','DSC','BBQ','SLB','BAS','LBO'],
			'LBO':['BAS','NLB','SLB','VIP','BYZ','SSS','PBO'],
			'LDK':['TRM','FAC','ADM','BAS'],
			'ADM':['LDK','FAC','WWS','BAS'],
			'STR':['BAB','CHL','OMM','DIH','WWS'],
			'WWS':['ADM','BAS','STR','DIH','CCC','SMS','NWH','DSC','BAS'],
			'NWH':['WWS','DSC','SMS','WHN','MED','BBQ'],
			'BBQ':['NWH','DSC','NLB','SLB','MED'],
			'SLB':['LBO','VIP','EHN','MED','BBQ','NLB'],
			'MED':['NWH','BBQ','SLB','TTT','WHN'],
			'WHN':['NWH','MED','TTT','WHE','SMS'],
			'DIH':['CCC','WWS','STR','OMM','FLG'],
			'CCC':['DIH','WWS','SMS','WHW','OFA'],
			'SMS':['WWS','NWH','WHN','WHW'],
			'WHW':['CCC','SMS','WHE','NGL'],
			'VIP':['SLB','LBO','EHN','BYZ'],
			'EHN':['SLB','VIP','BYZ','TTT','EHE'],
			'BYZ':['VIP','LBO','SSS','EHE','EHN'],
			'EHE':['EHN','BYZ','SSS','SGL','EHW'],
			'EHW':['TTT','EHE','CHL','EWF','WHE'],
			'NGL':['OFA','WHW','EWF','SHL'],
			'FLG':['MSO','OMM','DIH','PML'],
			'EWF':['NGL','WHE','EHW','CHL','SHL'],
			'CHL':['EWF','EHW','SGL','LCC','KAT','SHL'],
			'SGL':['CHL','EHE','SSS','LCC'],
			'SHL':['OFA','NGL','EWF','CHL','KAT'],
			'SSS':['SGL','EHE','BYZ','LBO','PBO','BBO','LCC'],
			'PBO':['LBO','SSS','BBO','OSO'],
			'BBO':['DIT','LCC','SSS','PBO','OSO','MEM','OCR'],
			'OFA':['PML','CCC','NGL','SHL','OCR','ADM'],
			'PML':['LAS','MSO','FLG','OFA','ADM','MEZ','LIB','ROD'],
			'ADM':['PML','OFA','OCR','SSA','MEZ'],
			'OCR':['KAT','MEM','FOF','SSA','ADM'],
			'KAT':['SHL','CHL','LCC','DIT','OCR'],
			'DIT':['KAT','LCC','BBO'],
			'MEM':['FOF','OCR','BBO','NML'],
			'SSA':['OVL','LIB','MEZ','ADM','OCR','FOF','SWP'],
			'FOF':['SSA','OCR','MEM','NML','SWP'],
			'NML':['FOF','MEM','OSO','SWP'],
			'SWP':['OVL','SSA','FOF','NML','OSO','WEH','OWO'],
			'OSO':['NML','BBO','PBO','OWO','WEH','SWP'],
			'OWO':['SLA','NLA','OVL','SWP','WEH','OSO'],
			'WEH':['SWP','OSO','OWO'],
			'OVL':['OWO','NLA','HDK','LIB','SSA','SWP'],
			'SLA':['NLA','OWO'],
			'NLA':['OBC','BSF','ENT','HDK','OVL','OWO','SLA'],
			'OBC':['BLF','NEE','BSF','NLA'],
			'BLF':['ESC','NEE','OBC'],
			'ESC':['BLF','NEE','STE'],
			'ENT':['NLA','BSF','SAC','ROD','HDK'],
			'HDK':['NLA','ENT','ROD','LIB','OVL'],
			'LIB':['HDK','ROD','PML','MEZ','SSA','OVL'],
			'MEZ':['LIB','PML','ADM','SSA'],
			'ROD':['ENT','SAC','MAC','CAC','CHL','LAS','PML','LIB','HDK'],
			'SAC':['BSF','LPB','MAC','ROD','ENT'],
			'MAC':['LPB','CAC','ROD','SAC'],
			'LPB':['NEE','SBO','BAJ','CAC','MAC','SAC'],
			'BSF':['OBC','LPB','SAC','ENT','NLA'],
			'NEE':['BLF','ESC','STE','SBO','LPB','OBC'],
			'SBO':['NEE','STE','HPV','BAJ','LPB'],
			'STE':['ESC','HPV','SBO','NEE'],
			'HPV':['STE','BAB','VMO','BAJ','SBO']
			'BAJ':['SBO','HPV','VMO','CAC','LPB'],
			'VMO':['HPV','BAB','MCR','BAJ']}
		self.fall = True
		
		
	
			
	def update(self, actions):
		pass
		
		
	def reset_troops (self):
		pass

	#round grabs all the moves from the countries and categorizes them. It then runs the supports to addall the strengths. Then it checks if the convoys go through. 
	#Finally it takes the updated attacks and sees which will actually go through. Finally it checks all the approved attacks to see if there are any conflicts. 
	# Then it updates all the countries. 
	def turn(self):
		round_actions=[]
		attacks = {}
		supports = {}
		convoys = {}
		approved_attacks = []
		final_attacks = []
		self.fall = not self.fall

		#CHANGED self.countries to list of countries with lists of actions!
		for country in self.countries:
			#How do I clear round actioms?
			#CHANGED HERE TO
			actions = country.get_actions()
			for action in actions:
				round_actions.append(action)
				if action[1] == "attack":
					attacks[action[0]] = action
				if action[1] == "support":
					supports[action[0]] = action
				if action[1] == "convoy":
					convoys[action[0]] = action
		#self.attacks(attacks)
		attacks,convoys = self.resolve_supports(supports, attacks, convoys)
		attacks = self.resolve_convoys(convoys, attacks)
		approved_attacks = self.resolve_attacks(attacks, convoys, supports)
		#for attack in approved_attacks:
			#print attack
		list_attacks = []
		for attack in attacks:
			list_attacks.append(attacks[attack])
		final_attacks = self.update(list_attacks) 
		
		for country in self.countries:
			country.update(final_attacks[0], final_attacks[1],self)
			
		return final_attacks
		#Do non attack retreats




	#Takes a move and the attacks in that turn and checks if the attacks will affect this move and make it not happen. If there appears to be conflict it checks 
	def check_conflict (self, move, attacks):
		for attack in attacks:

			if attacks[attack][2] == move[0]:
				if not self.check_conflict( attacks[attack], attacks):
					return True
		return False



	def resolve_supports (self, supports, attacks, convoys):
		deletes = []
		for support in supports:
			if not self.check_conflict(supports[support], attacks):
				for attack in attacks:
					if supports[support][2] == attacks[attack][2] and supports[support][4] == attacks[attack][0]:
						attacks[attack][3] += 1
				for convoy in convoys:
					if supports[support][4] == convoys[convoy][0] and supports[support][2] == convoys[convoy][2]:
						convoys[convoy][3] +=1
			else: 
				#print supports[support]
				attacks[supports[support][0]] = [supports[support][0], "attack" , supports[support][0], 1, None, supports[support][5]]
				deletes.append(support)
		for delete in deletes:
			del supports[support] 
							
		return (attacks,convoys)
	
	def resolve_convoys (self, convoys, attacks):
		for convoy in convoys:
			#IF there is a conflict, change the attack so it doesn't move. 
			if self.check_conflict(convoys[convoy], attacks):
				if convoys[convoy][4] in attacks:
					#BUG
					if convoys[convoy][2] == attacks[convoys[convoy][4]][2]:
						attacks[convoys[convoy][4]][2] = attacks[convoys[convoy][4]][0]
		
		for attack in attacks:
			if attacks[attack][2] not in self.locations[attacks[attack][0]]:
				#check if being convoyed
				for convoy in convoys:
					if attacks[attack][0] == convoys[convoy][4] and attacks[attack][2] == convoys[convoy][2]:
						atk = True
				if not atk:
					attacks[attack][2] = attacks[attack][0]		
		return attacks

	def resolve_attacks (self, attacks, convoys, supports):
		approved_attacks =[]
		for attack in attacks:
			if self.approve_attack(attacks[attack], attacks, convoys, supports) or attacks[attack][0] == attacks[attack][2]:
				approved_attacks.append(attacks[attack])
		return approved_attacks
		
	
	def approve_attack (self, move, attacks, convoys, supports):
		#Check if place being attacked is even occupied, if not just approve attack(resolve two different attacks later)
		if move[2] in attacks:
			#if space is occupied, check the strengths. 
			#if the attack strength is stronger, approve attack, repeat for convoys and supports
			if move[3] > attacks[move[2]][3]:
				return True
			else:
				return False

		elif move[2] in convoys:
			if move[3] > convoys[move[2]][3]:
				return True
			else:
				return False
		elif move[2] in supports:
			if move[3] > convoys[move[2]][3]:
				return True
			else:
				return False 
		else:
			return True  
	
	def update (self, attacks):
		final_attacks = []
		incomplete = [] 
		waitlist = []
		next_list = attacks
		#while not next_list == []:
		for atk in next_list:
			conflict = False
			retreat = False
			#attacked = False
			cancelled = False
			wait = False
			for atk2 in next_list:
				if not atk == atk2:
					if atk[2] == atk2[2]: #If both have same destination
						if atk[3] < atk2[3]:
							#If the second attack is stronger and they're going to the same place, we either make a hold into a retreat or cancel an attack. 
							if atk[0] == atk[2]:
								retreat = True
							else:
								cancelled = True
								atk[2] = atk [0]
								atk[3] = 1
								#if they're strength are  equal if atk2 is holding atk cancelled. else there is a conclict. 
						elif atk[3] == atk2[3]:
							if atk2[2] == atk2[0]:
								cancelled = True
								atk[2] = atk [0]
								atk[3] = 1
							else:
								conflict = True
								atk[2] = atk[0]
								atk[3] = 1
								atk2[2] = atk2[0]
								atk2[3] = 1
							

					elif atk[2] == atk2[0]:
						if atk2[2] == atk[0]:
							if atk[3] < atk2[3]:
								retreat = True
							elif atk[3] == atk2[3]:
								conflict = True
								atk[2] = atk[0]
								atk[3] = 1
								atk2[2] = atk2[0]
								atk2[3] = 1
						else:
							wait = True
						
			if not conflict and not retreat and not wait and not cancelled:
				final_attacks.append(atk)
			if retreat:
				incomplete.append(atk)
			if wait:
				waitlist.append(atk)
		# Remove moves from list of attacks that are approved or require more user input
		for move in final_attacks:
			del next_list[next_list.index(move)]
		for move in incomplete:
			del next_list[next_list.index(move)]
		#for move in waitlist:
		#	del next_list[next_list.index(move)]

		if next_list == waitlist:
			final_attacks.extend(waitlist)
			return [final_attacks, incomplete]
		else:
			#for move in waitlist:
			#	next_list.append(move)
			update_return = self.update(next_list)
			for attack in update_return[0]:
				final_attacks.append(attack)
			for incomp in update_return[1]:
				incomplete.append(incomp)
			return [final_attacks, incomplete]
			

	def update_supply(self):
		loc_list = []
		sup_list = []
		for country in self.countries:
			for loc in country.locations:
				loc_list.append([loc, country])
			for sup in country.supply:
				sup_list.append([sup, country])
		
		for loc in loc_list:
			for sup in sup_list:
				if loc[0] == sup[0]:
					sup[1] = loc[1]
		
		for country in self.countries:
			country.supply = []
		
		for sup in sup_list:
			sup[1].supply.append(sup[0])

#if attacking its strength cannot defend it 
#update non attack

					#if [atk][0]
					#	if conflict
#						pass
					


		#check for two things entering the same spot

	
			#Attack 

#[Current Location, "attack", Location attacking, 1, None ,Country]
if __name__ == "__main__":
		
	country1 = [["1", "attack", "2", 1, None, []],["3", "support", "2", 1, "1", []],["10", "attack", "11", 1, None, []], ["11", "attack", "12", 1, None, []], ["12", "attack", "10", 1, None, []]]
	country2 = [["2", "attack", "2", 1, None,[]],["4", "attack", "13", 1, None, []], ["9", "attack", "3", 1, None, []] ]
	country3 = [["5","convoy", "7", 1, "6", []],["6", "attack", "7", 1, None, []], ["8", "attack", "5", 1, None, []]]
	countries = (country1, country2, country3)
	 #[this place, support, where the place is going, strength, who is going there]
	#for convoy support  [this place, support, where the army is going, strength, where the ship is]
	# convoy [place, convoy, where thing is going, str, who is going ]
	wo = world(countries)
	wo.round()
	
	print "hi"



	
	
	def test ():
		#test Hold and unobjected attackS

		country1 = [["1", "attack", "3", 1, None, []]]
		country2 = [["2", "attack", "2", 1, None,[]]]
		expected_result = [["1", "attack", "3", 1, None, []], ["2", "attack", "2", 1, None,[]]]
		expected_result.sort() 
		wo1 = world(countries)
		results  = wo1.round()
		results.sort() 
		if not results == expected_result:
			print "Failed Test1, Holds and unobjected attacks"

		#test attackS


		# 
		country1 = [["1", "attack", "2", 1, None, []],["3", "attack", "5", 1, None, []],["4", "attack", "5", 1, "4", []], ]
		country2 = [["2", "attack", "2", 1, None,[]],["5", "attack", "5", 1, None, []]]
		expected_result = [["1", "attack", "3", 1, None, []], ["2", "attack", "2", 1, None,[]]]
		expected_result.sort() 
		wo1 = world(countries)
		results  = wo1.round()
		results.sort() 
		if not results == expected_result:
			print "Failed Test1, Holds and unobjected attacks"


		


#
