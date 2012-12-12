from PIL import ImageDraw, Image
#import DipConts
	#Gets moves[[Location, Color],[]] a where things currently are. 
def update_map (countries, file):
	im = Image.open(file)
	draw = ImageDraw.Draw(im)
	#pix = im.load()
	#width, height = im.size
	color_dict = {"Aqua":(84,255,159),"Brown":(142,107,35),"Red":(255,0,0),"Orange":(255,127,0),"Purple":(128,0,128), "White": (255,255,255)}
	paste_loc ={} 		
	fin = open("Abr_Name_PixLoc", "r")
	for line in fin:
		info = line.split("-")
		if len(info[2].split(",")) > 1:
			coordinate = info[2].split(",")
			x = int(coordinate[0].strip())
			y = int(coordinate[1][:-1].strip())
			paste_loc[info[0]] = (x,y)

	print paste_loc
	for country in countries:
		for location in country.locations:
			x,y = paste_loc[location[0]]
			if location[1] == "A":
				draw.rectangle([x,y,x+20, y+10], fill = color_dict[country.color])
				if location[0] in country.supply:
					#draw.line([x,y, x+20, y +10], fill = color_dict["White"], width = 1)
					#draw.line([x+20,y, x, y+10], fill = color_dict["White"], width = 1)
					draw.chord([x+7,y+2, x+13, y+8],0,360,fill = color_dict["White"])
					
			else:
				draw.polygon([x+10,y, x+20, y+10, x, y+10, x+10,y ], fill = color_dict[country.color] )
				if location[0] in country.supply:
					#draw.line([x-10, y , x+10, y +10], fill = color_dict["White"], width = 1)
					#draw.line([x-10, y +10 , x+10, y], fill = color_dict["White"], width = 1)
					draw.chord([x+7,y+3, x+13, y+9],0,360,fill = color_dict["White"])
					
	stuff = {'BAB':['TRM','FAC','VMO','MCR','CHL','STR'],
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
	for location in stuff:
			x,y = paste_loc[location]
			draw.rectangle([x,y,x+20, y+10], fill = color_dict["White"])	
	print stuff 
	im.save("edited.png")

			#im.paste(paste, tlcorner)
"""			
	#im.op("testmap.png")

	for move in locs:
		tlcorner = DipConts.center_pixels[move[0]]
		paste = Image.open(move[1][0]+"square.png")
		im.paste(paste, tlcorner)
		#for xdelta in range(4):
		#	for ydelta in range(4): 
		#		pix[x+xdelta, y + ydelta] = DipConts.colors[move[1]]
		#		pix[x+xdelta, y + ydelta] = DipConts.colors[move[1]]
"""



"""m.paste(image, box)

Pastes another image into this image. The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted image must match the size of the region.

If the modes don't match, the pasted image is converted to the mode of this image (see the convert method for details).

im.paste(colour, box)

Same as above, but fills the region with a single colour. The colour is given as a single numerical value for single-band images, and a tuple for multi-band images.
"""