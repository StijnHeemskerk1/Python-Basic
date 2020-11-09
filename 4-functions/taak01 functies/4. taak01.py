#vraag1: Zodat ze in de hele code kunnen worden aangesproken.
def keerdelistom(x):
  for i in reversed(x):
    print(i, end= " ")
    print()
  return

a = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
keerdelistom(a)

#vraag2: reversed() zorgt ervoor dat een list van achter naar voren wordt geprint

#opdracht1
Ce = 25
def celcius2fahren(Ce):
  return (Ce * 9 / 5 + 32)

print("de temperatuur van", Ce, "graden Celcius is", celcius2fahren(Ce), "graden Fahrenheit")


