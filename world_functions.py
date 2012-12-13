class world (object):
	
	# Has list of all the supply centers, list of all oceans, dictionary that maps from each land location to its adjacent land locations, and dictionary that maps from each water location to its adjacent locations. 
	def __init__ (self, countries):
		self.countries = countries
		self.supplys = ['CAC', 'MAC','SAC', 'MCR', 'LIB', 'MEZ', 'ADM', 'DIH', 'FAC', 'LDK', 'WHW', 'WHE', 'WHN', 'EHE', 'EHN', 'EHW', 'NGL', 'CHL', 'LCC', 'KAT', 
		'NGL', 'TTT', 'NWH', 'BBQ', 'SLB', 'SLR', 'WEH', 'NML', 'SSA', 'LAS', 'MSO', 'ROD', 'BAB', 'TRM', 'ESC', 'HDK', 'SLA', 'BSF', 'BLF', 'ESC' ]

		self.waterlist  = ['OVL', 'OWO', 'OSO', 'BABO', 'OCR', 'OFA', 'CCC', 'WWS', 'BAS', 'LBO', 'SSS', 'PBO' , 'BAJ', 'HPV', 'SBO']
		
		self.locations = {'BAB':['TRM','FAC','VMO','MCR','CHL','STR'],
			'CHR':['BAB','MCR','CAC','LAS','OMM','STR','ROD'],
			'MCR':['VMO','CAC','CHR','BAB'],
			'CAC':['MCR','CHR','LPB','MAC','ROD'],
			'LAS':['CHR','PML','MSO','ROD'],
			'MSO':['LAS','OMM','FLG','PML'],
			'OMM':['CHR','STR','DIH','MSO'],
			'TRM':['BAB','LDK','FAC'],
			'FAC':['LDK','TRM','BAB','STR','ADM'], 
			'WHE':['WHN','WHW','TTT','EHW','EWF'],
			'TTT':['MED','WHN','WHE','EHW','EHN'],
			'SLR':['NLB','DSC'],
			'DSC':['SLR','NLB','BBQ','NWH'],
			'NLB':['SLR','DSC','BBQ','SLB'],
			'LDK':['TRM','FAC','ADM'],
			'ADM':['LDK','FAC'],
			'STR':['BAB','CHR','OMM','DIH'],
			'NWH':['DSC','SMS','WHN','MED','BBQ'],
			'BBQ':['NWH','DSC','NLB','SLB','MED'],
			'SLB':['VIP','EHN','MED','BBQ','NLB'],
			'MED':['NWH','BBQ','SLB','TTT','WHN'],
			'WHN':['NWH','MED','TTT','WHE','SMS'],
			'DIH':['STR','OMM','FLG'],
			'SMS':['NWH','WHN','WHW'],
			'WHW':['SMS','WHE','NGL'],
			'VIP':['SLB','EHN','BYZ'],
			'EHN':['SLB','VIP','BYZ','TTT','EHE'],
			'BYZ':['VIP','EHE','EHN'],
			'EHE':['EHN','BYZ','SGL','EHW'],
			'EHW':['TTT','EHE','CHL','EWF','WHE'],
			'NGL':['WHW','EWF','SHL'],
			'FLG':['MSO','OMM','DIH','PML'],
			'EWF':['NGL','WHE','EHW','CHL','SHL'],
			'CHL':['EWF','EHW','SGL','LCC','KAT','SHL'],
			'SGL':['CHL','EHE','LCC'],
			'SHL':['NGL','EWF','CHL','KAT'],
			'PML':['LAS','MSO','FLG','ADM','MEZ','LIB','ROD'],
			'ADM':['PML','SSA','MEZ'],
			'KAT':['SHL','CHL','LCC','DIT'],
			'DIT':['KAT','LCC'],
			'MEM':['FOF','NML'],
			'SSA':['LIB','MEZ','ADM','FOF','SWP'],
			'FOF':['SSA','MEM','NML','SWP'],
			'NML':['FOF','MEM','SWP'],
			'SWP':['SSA','FOF','NML','WEH'],
			'WEH':['SWP'],
			'SLA':['NLA'],
			'NLA':['OBC','BSF','ENT','HDK','SLA'],
			'OBC':['BLF','NEE','BSF','NLA'],
			'BLF':['ESC','NEE','OBC'],
			'ESC':['BLF','NEE','STE'],
			'ENT':['NLA','BSF','SAC','ROD','HDK'],
			'HDK':['NLA','ENT','ROD','LIB'],
			'LIB':['HDK','ROD','PML','MEZ','SSA'],
			'MEZ':['LIB','PML','ADM','SSA'],
			'ROD':['ENT','SAC','MAC','CAC','CHR','LAS','PML','LIB','HDK'],
			'SAC':['BSF','LPB','MAC','ROD','ENT'],
			'MAC':['LPB','CAC','ROD','SAC'],
			'LPB':['NEE','CAC','MAC','SAC'],
			'BSF':['OBC','LPB','SAC','ENT','NLA'],
			'NEE':['BLF','ESC','STE','LPB','OBC'],
			'STE':['ESC','NEE'],
			'VMO':['BAB','MCR'],
			'LCC':['KAT','DIT','SGL','CHL']}

		self.water = {
			'SLA':['NLA','OWO'],
			'NLA':['SLA','HDK','OWO','OVL'],
			'HDK':['NLA','LIB','OVL'],
			'LIB':['HDK','SSA','OVL'],
			'SSA':['LIB','ADM','OCR','FOF','SWP','OVL'],
			'SWP':['OWO','OVL','SSA','FOF','NML','OSO','WEH'],
			'WEH':['OWO','SWP','OSO'],
			'OVL':['NLA','HDK','LIB','SSA','SWP','OWO'],
			'OWO':['SLA','NLA','OVL','SWP','WEH','OSO'],
			'OSO':['OWO','WEH','SWP','NML','BABO','PBO'],
			'NML':['SWP','FOF','MEM','OSO'],
			'FOF':['SSA','OCR','MEM','NML'],
			'MEM':['NML','FOF','OCR','BABO'],
			'ADM':['SSA','PML','OFA','OCR'],
			'PML':['ADM','OFA'],
			'DIH':['CCC'],
			'STR':['WWS'],
			'AND':['WWS','LDK','BAS'],
			'LDK':['AND','TRM','BAS'],
			'TRM':['LDK','BAS'],
			'BAS':['TRM','LDK','AND','WWS','SLR','NLB'],
			'SLR':['DSC','NLB','BAS'],
			'DSC':['SLR','NWH','WWS'],
			'NWH':['WWS','DSC','SMS'],
			'SMS':['WWS','NWH','WHW','CCC'],
			'WHW':['SMS','CCC','NGL'],
			'NGL':['WHW','OFA','SHL'],
			'SHL':['NGL','OFA','KAT'],
			'KAT':['SHL','OCR','DIT'],
			'DIT':['KAT','BABO','LCC'],
			'LCC':['DIT','BABO','SGL','SSS'],
			'SGL':['LCC','EHE','SSS'],
			'EHE':['SGL','BYZ','SSS'],
			'BYZ':['VIP','LBO','SSS','EHE'],
			'VIP':['SLB','LBO','BYZ'],
			'SLB':['NLB','LBO','VIP'],
			'NLB':['SLR','BAS','LBO','SLB'],
			'LBO':['BAS','NLB','SLB','VIP','BYZ','SSS','PBO'],
			'PBO':['LBO','SSS','BABO','OSO'],
			'SSS':['LBO','BYZ','EHE','SGL','LCC','BABO','PBO'],
			'BABO':['LCC','SSS','PBO','OSO','MEM','OCR','DIT'],
			'OCR':['SSA','ADM','OFA','KAT','BABO','MEM','FOF'],
			'OFA':['OCR','ADM','PML','CCC','NGL','SHL'],
			'CCC':['DIH','WWS','SMS','WHW'],
			'WWS':['STR','AND','DSC','NWH','SMS','CCC'],
			'STE':['NEE','SBO','HPV'],
			'NEE':['STE','SBO','LPB'],
			'LPB':['NEE','SBO','BAJ','CAC'],
			'CAC':['LPB','BAJ'],
			'VMO':['BAJ','HPV','BAB'],
			'BAJ':['HPV','VMO','CAC','LPB','SBO'],
			'SBO':['STE','NEE','LPB','BAJ','HPV'],
			'HPV':['STE','SBO','BAJ','BAB']}
		self.fall = True
		
		

	# turn() grabs all the moves from the countries and categorizes them. It then runs the supports to add all the strengths. 
	# Then, it checks if the convoys go through. Then, it takes the updated attacks and sees which will actually go through. 
	# It checks all the approved attacks to see if there are any conflicts between seperate attacks. 
	#  Finally, it updates all the countries with their new locations and supply centers. 
	def turn(self):
		round_actions=[]
		attacks = {}
		supports = {}
		convoys = {}
		approved_attacks = []
		final_attacks = []
		self.fall = not self.fall
		#Put all the moves in dictionaries
		for country in self.countries:
			actions = country.get_actions()	

			for action in actions:
				round_actions.append(action)
				
				if action[1] == "attack":
					attacks[action[0]] = action
				if action[1] == "support":
					supports[action[0]] = action
				if action[1] == "convoy":
					convoys[action[0]] = action

		# for each type of move, resolve them
		attacks,convoys = self.resolve_supports(supports, attacks, convoys)
		attacks = self.resolve_convoys(convoys, attacks)
		#The difference between resolve attacks and update is that resolve attacks checks whether the attack is being cut off or cancelled 
		#while update checks if the attack conflicts with other attacks.   
		approved_attacks = self.resolve_attacks(attacks, convoys, supports)
		
		#switch from a dictionary to a list

		list_attacks = []
		for attack in attacks:
			list_attacks.append(attacks[attack])
		
		final_attacks = self.update(list_attacks) 
		
		for country in self.countries:
			country.update(final_attacks[0], final_attacks[1],self)

		return final_attacks




	#Takes a move and the attacks in that turn and checks if the attacks will affect this move and cause it not to happen. 
	#If there appears to be conflict it checks, if the conflicting attack has a conflict recursively
	def check_conflict (self, move, attacks):
		for attack in attacks:
			if attacks[attack][2] == move[0]:
				if not self.check_conflict( attacks[attack], attacks):
					return True
		return False


	# This goes through each support, checks if it is conflicted, and if it is oked, increases the strength of the move that is being supported	
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
				attacks[supports[support][0]] = [supports[support][0], "attack" , supports[support][0], 1, None, supports[support][5]]
				deletes.append(support)
		for delete in deletes:
			del supports[support] 
							
		return (attacks,convoys)

	#Goes through each convoy, checks for conflicts. If there is a conflict, it cancels the attack being convoyed.
	def resolve_convoys (self, convoys, attacks):
		for convoy in convoys:
			#IF there is a conflict, change the attack so it doesn't move. 
			if self.check_conflict(convoys[convoy], attacks):
				if convoys[convoy][4] in attacks:
					if convoys[convoy][2] == attacks[convoys[convoy][4]][2]:
						attacks[convoys[convoy][4]][2] = attacks[convoys[convoy][4]][0]
		
		for attack in attacks:
			atk = True
			#checking if its trying to move to non-adjacent spot. if so, need convoy 
			if attacks[attack][2] not in self.locations[attacks[attack][0]]:
				atk = False
				#check if being convoyed
				for convoy in convoys:
					if attacks[attack][0] == convoys[convoy][4] and attacks[attack][2] == convoys[convoy][2]:
						atk = True

				if not atk:
					attacks[attack][2] = attacks[attack][0]		
		return attacks
	#Checks if move is apprive or is a hold. Returns all the approved attacks. 
	def resolve_attacks (self, attacks, convoys, supports):
		approved_attacks =[]
		for attack in attacks:
			if self.approve_attack(attacks[attack], attacks, convoys, supports) or attacks[attack][0] == attacks[attack][2]:
				approved_attacks.append(attacks[attack])
		return approved_attacks
		
	#This checks approves attack by checking if it is attacking an occupied place. If not, they're approved. If so, we check who'd win then decide.
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
	#This takes the appoved attacks and checks fo diffeent types of conflicts. For each attack, they're either approved, cancelled, delayed 
	#(wait  until the destination is set before figuing out what to do)  
	def update (self, attacks):
		final_attacks = []
		incomplete = [] 
		waitlist = []
		next_list = attacks
		for atk in next_list:
			conflict = False
			retreat = False
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
		
		if next_list == waitlist:
			final_attacks.extend(waitlist)
			return [final_attacks, incomplete]
		else:
			update_return = self.update(next_list)
			for attack in update_return[0]:
				final_attacks.append(attack)
			for incomp in update_return[1]:
				incomplete.append(incomp)
			return [final_attacks, incomplete]
		
	#This updates which each countries supply centers based on the completed attacks. 
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
			if [loc[0],loc[1]] not in sup_list and loc[0] in self.supplys:
				sup_list.append([loc[0], loc[1]])
		
		for country in self.countries:
			country.supply = []
		
		for sup in sup_list:
			sup[1].supply.append(sup[0])