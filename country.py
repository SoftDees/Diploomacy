import random
class Country(object):
    

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

    
