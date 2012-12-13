from PIL import ImageDraw, Image

# This function takes in countries and upates the map based on these countries

def update_map (countries, file):
	
	# Open the file, make draw object, and make a dictionary of colors to their rgb
	im = Image.open(file)
	draw = ImageDraw.Draw(im)
	color_dict = {"Aqua":(84,255,159),"Brown":(142,107,35),"Red":(255,0,0),"Orange":(255,127,0),"Purple":(128,0,128), "White": (255,255,255)}
	paste_loc ={} 		

	# Open the file that holds all our abreviation, full name and pixel location(for where to put a marker in the picture).

	fin = open("Abr_Name_PixLoc", "r")
	for line in fin:
		info = line.split("-")
		if len(info[2].split(",")) > 1:
			# Grab the x,y coordinates, put them in the dictionary as the item with the abreviation of the location as the key 
			coordinate = info[2].split(",")
			x = int(coordinate[0].strip())
			y = int(coordinate[1][:-1].strip())
			paste_loc[info[0]] = (x,y)

	
	for country in countries:
		# Draw a colored dot in all the supply centers this country owns
		for supplycenter in country.supply:
			x,y = paste_loc[supplycenter]
			draw.chord([x+7,y+3, x+13, y+9],0,360,fill = color_dict[country.color])
					
		# Draw a rectangle or triangle in each location of the country. It also draws a white circle signifying a supply center if needed (because the previous ones have been covered. 
		for location in country.locations:
			x,y = paste_loc[location]
			if country.locations[location] == "A":
				draw.rectangle([x,y,x+20, y+10], fill = color_dict[country.color])
				if location in country.supply:
					draw.chord([x+7,y+3, x+13, y+9],0,360,fill = color_dict["White"])
						
			else:
				draw.polygon([x+10,y, x+20, y+10, x, y+10, x+10,y ], fill = color_dict[country.color] )
				if location in country.supply:
					draw.chord([x+7,y+3, x+13, y+9],0,360,fill = color_dict["White"])
	im.show()			
	im.save("edited.png")
	