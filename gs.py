from country import *
from world_functions import *
from make_map import *
ACL = {"SAC": "A", "MAC": "A", "CAC": "F", "MCR": "A"}
ACS = ["SAC", "MAC", "CAC", "MCR"]

CCL = {"LDK": "F","FAC": "A","DIH": "A"}
CCS = ["LDK", "FAC", "DIH"]

MHL = {"LIB": "A","MEZ": "A","ADM": "F"}
MHS = ["LIB","MEZ","ADM"]

WHL = {"WHN": "A" , "WHW":"F", "WHE":"A"}
WHS = ["WHN", "WHW", "WHE"]

EHL = {"EHN": "A","EHW":"A","EHE":"F"}
EHS = ["EHN", "EHW", "EHE"]

#Locations, supply, Name, usrname
AC = Country(ACL, ACS, "ACPlayer", "AC", "Aqua")
CC = Country(CCL, CCS, "CCPlayer", "CC", "Orange")
MH = Country(MHL, MHS, "MHPlayer", "MH", "Brown")
WH = Country(WHL, WHS, "WHPlayer", "WH", "Red")
EH = Country(EHL, EHS, "EHPlayer", "EH", "Purple")

countries = [AC,CC,MH, WH, EH]
wo = world(countries)
update_map(wo.countries, "BaseMap.png")
#EH.move('EHN', 'SGL', wo)
#EH.convoy('EHE', 'SGL', 'EHN', wo)
#EH.move('EHW', 'TTT', wo)
MH.move('LIB', 'HDK', wo)
MH.move('MEZ', 'SSA', wo)
MH.move('ADM', 'OCR', wo)

wo.turn()
update_map(wo.countries, "BaseMap.png")
MH.move('HDK', 'NLA', wo)
MH.move('SSA', 'KAT', wo)
MH.convoy('OCR', 'KAT', 'SSA', wo)

wo.turn()
update_map(wo.countries, "BaseMap.png")
#MH.move('LIB', 'ROD', wo)
start = raw_input("where")
end = raw_input("to where?")
MH.move(start,end,wo)
MH.move('NLA', 'SLA',wo)
MH.move('KAT', 'CHL',wo)

#EH.move('MED', 'BBQ', wo)
wo.turn()
update_map(wo.countries, "BaseMap.png")
start = raw_input("where")
end = raw_input("to where?")
MH.move(start,end,wo)
#EH.move('BBQ', 'MED', wo)
#WH.move('WHE', 'TTT', wo)
wo.turn()
update_map(wo.countries, "BaseMap.png")
#WH.move('TTT', 'WHE', wo)
#WH.move('WHW', 'WHN', wo)
#AC.move('MAC', 'BLF', wo)
#CC.move ('DIH', 'OMM', wo)
#AC.move('CAC','CHR', wo)
wo.turn()
update_map(wo.countries, "BaseMap.png")


print EH.locations

