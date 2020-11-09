#opgave1
Provinciehoofdsteden = dict([
('Noord_Holland' , 'Amsterdam'),
('Zuid_Holland', 'Den_Haag'),
('Utrecht', 'Utrecht'),
])
print(type(Provinciehoofdsteden))

#opgave2
for x in Provinciehoofdsteden:
  print(x, Provinciehoofdsteden[x])

#opgave3
Provinciehoofdsteden['Groningen'] = 'Groningen'
Provinciehoofdsteden['Drenthe'] = 'Assen'
Provinciehoofdsteden['Zeeland'] = 'Middelburg'
for x in Provinciehoofdsteden:
  print(x, Provinciehoofdsteden[x])

#opgave4
Provinciehoofdsteden['Zeeland'] = 'veranderd'
print(Provinciehoofdsteden['Zeeland'])
del Provinciehoofdsteden['Zeeland']
