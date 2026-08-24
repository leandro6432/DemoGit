from models.animal import Animal
from models.chat import Chat
from models.personne import Personne


p1 = Personne("spinosi","leandro")
p2= Personne("Bracke","Gwenel")
a1 = Animal("vache")
chat1 = Chat("mona", False)
p1.aj_ani(a1)
p2.aj_ani(chat1)
