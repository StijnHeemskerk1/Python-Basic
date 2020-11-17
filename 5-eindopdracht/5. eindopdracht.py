#Import de timer.
from threading import Timer

#Global variables van de uren, minuten en seconden in de timer.
sec = 50
min = 59
uur = 23

#De klok functie
def myClock():
  #Hier vraagt die de gegevens van de 3 globale variables aan en verhoogt die sec met 1.
  global sec
  global min
  global uur
  sec += 1
  #Hier checked de functie of sec 60 is zodat die sec kan resetten en min verhoogt met 1.
  if (sec == 60):
    min += 1
    sec = 0
    #Hier checked de functie of min 60 is zodat die min kan resetten en uur verhoogt met 1.
    if (min == 60):
      uur += 1
      min = 0
      #Hier checked de functie of uur 24 is zodat die de timer kan resetten om een nieuwe dag te starten.
      if (uur == 24):
        sec = 0
        min = 0
        uur = 0
  #In deze print worden de timer variablen strings gemaakt zodat ze vervolgens 2 getallen krijgen door .zfill(2) waardoor het er meer uit
  #ziet als een timer. Ook wordt hier een dubbele punt toegevoegd tussen de variablen.
  print(str(uur).zfill(2), ":", str(min).zfill(2), ":", str(sec).zfill(2))
  #Deze regel zorgt ervoor dat myClock() iedere 1 seconden wordt aangeroepen.
  Timer(1, myClock).start()

#Hier wordt de functie aan geroepen om de hele timer te beginnen.
myClock()

