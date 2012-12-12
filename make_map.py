from PIL import ImageDraw, Image


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
	for country in countries:
		for supplycenter in country.supply:
			x,y = paste_loc[supplycenter]
			draw.chord([x+7,y+3, x+13, y+9],0,360,fill = color_dict[country.color])
					
			 
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
	