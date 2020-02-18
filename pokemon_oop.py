




#aray of each pokemon do to others by type, fisrt list is normal type, seconed is Fire ect.

damage_array = ([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                               [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])

pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
      
#class for pokemon, each obj will be pokemon
class Pokemon():
  
  def __init__(self,name,level,p_type,health,max_health,exp=0):
    
    self.name=name
    self.level=level
    self.type=p_type
    self.health=health
    self.max_health=max_health
    self.exp=exp
    #it check that the pokemon actually alive
    if self.health>0:
      self.is_knocked_out=False
    else:
      self.is_knocked_out=True
     # it create a couples of advatnage of this type compare to other types of pokemon, and when he attack it influence the damage 
    self.advantage=dict(zip(pokemon_types,damage_array[pokemon_types.index(self.type)]))
    
  def __repr__(self):
    return " {}, level {}, {},health {}, max health {}, {}".format(self.name,self.level,self.type,self.health,self.max_health,self.is_knocked_out)
      
# get health
  def gain_health(self,gain):
    self.health+=gain
    if self.health<=self.max_health:
      print("{} now has {} health".format(self.name,self.health))
    else:
      self.health=self.max_health
      print("{} now has {} health".format(self.name,self.health))
    if self.is_knocked_out==True:
      self.revive()
    #loose health in the end check if he dead
    
  def decrease(self,decrease):
    self.health-=decrease
    print("{} now has {} health".format(self.name,self.health))
    self.knock_out()
    
  def knock_out(self):
    if self.health<=0:
      self.is_knocked_out=True
      print("{} is dead".format(self.name))
      
    
  def revive(self,new_health):
     
    if self.is_knocked_out == True:
      self.is_knocked_out = False
      self.health = new_health
      print(self)
    else: 
        print("{} is still alive,no need to revive".format(self.name))
        
  def attack(self,another_pokemon):
    
    if self.is_knocked_out == False and another_pokemon.is_knocked_out == False:
      damage=int(round(self.level*self.advantage[another_pokemon.type]))
      another_pokemon.health-=damage
      self.exp+=int(round(damage/2))
      
      
      print("you did damage of {} , {} have {} health".format(damage,another_pokemon.name,another_pokemon.health))
      #check if the other pokemon should be dead
      another_pokemon.knock_out()
      #update level and exp
      self.level_check()
    else:
      print("players cant attack if one pokemon is knock out")
  
  
  def level_check(self):
    if self.exp>20:
      self.level+=1
      new_exp=self.exp%20
      self.exp=new_exp
      print("{} new level is {} with {} exp".format(self.name,self.level,self.exp))
    else:
      print("{} have {} exp".format(self.name,self.exp))


class Charmander(Pokemon):
  def __init__(self,name,level,p_type,health,max_health,exp=0,rounds=2):
    super().__init__(name,level,p_type,health,max_health,exp=0)
    self.rounds=rounds
  
  def __repr__(self):
    return " {}, level {}, {},health {}, max health {}, {}, {}".format(self.name,self.level,self.type,self.health,self.max_health,self.is_knocked_out,self.rounds)
    
  
  def round_the_world(self):
    if self.rounds>0:
      self.rounds-=1
      self.health=self.max_health
      print("{} did round around the world and have max health of {}".format(self.name,self.health))
    else:
      print("you dont have rounds to use")
    
 
  
      

class Trainer():
  def __init__(self,pokemons,name,potions,active_pokemon):
    self.pokemons=pokemons
    self.name=name
    self.potions=potions
    self.active_pokemon=active_pokemon
  def __repr__(self):
    a=[]
    for i in self.pokemons:
      a.append(i.name)
    return "{} ,{}, {}, {}".format(a,self.name,self.potions,self.active_pokemon)
  
  def use_potion(self):
    if self.potions>0:
      self.active_pokemon.health+=10
      self.potions-=1
    if self.active_pokemon.health>self.active_pokemon.max_health:
      self.active_pokemon.health=self.active_pokemon.max_health
    print("you used potion on",self.active_pokemon.name,"he got now",self.active_pokemon.health,"health")
    print("{} have {} potions left".format(self.name,self.potions))
    if self.active_pokemon.is_knocked_out==True:
      self.active_pokemon.revive(10)
    
  def attack(self,another_trainer):
    print ("You attack {}, his active pokemon is {}".format(another_trainer.name,another_trainer.active_pokemon.name))
    self.active_pokemon.attack(another_trainer.active_pokemon)
  def switch(self,active):
    if active in self.pokemons and active.is_knocked_out==False:
      self.active_pokemon=active
      print("you changed active pokemon, to {}".format(self.active_pokemon))
    else:
      print("this pokemon not availible")
      
  def add_pokemon(self,pokemon):
      if type(pokemon)==Pokemon or type(pokemon)==Charmander:
        self.pokemons.append(pokemon)
        print("{} add one pokemon".format(self.name))
      else:
        print("it's not a pokemon")
    
    








picathu=Pokemon("picathu",5,"Electric",20,30)

charmander=Charmander("charmander",7,"Fire",20,40)

lizi=Pokemon("lizi",9,"Dragon",20,40)
tai=Pokemon("tai",9,"Flying",10,15)


donio=Trainer([picathu,charmander],'donio',5,picathu)


margot=Trainer([lizi,tai],'margot',6,lizi)

#first game:
print(picathu)
picathu.gain_health(10)
picathu.decrease(5)
picathu.knock_out()
print(charmander)
picathu.attack(charmander)
print(picathu.advantage)
print(donio)
donio.use_potion()
margot.attack(donio)
donio.switch(charmander)
cati=Pokemon("cati",4,"Steel",20,40)
margot.add_pokemon(cati)
margot.add_pokemon(5)
margot.switch(cati)
margot.attack(donio)
margot.attack(donio)
margot.attack(donio)
margot.switch(lizi)
margot.attack(donio)
margot.attack(donio)
donio.use_potion()
print(donio.active_pokemon)
margot.attack(donio)
margot.attack(donio)
donio.switch(picathu)
donio.switch(charmander)
margot.attack(donio)
margot.attack(donio)
margot.attack(donio)
charmander.revive(10)
charmander.round_the_world()
donio.switch(charmander)
