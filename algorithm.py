# -*- coding: utf-8 -*-
import random

schenkernamen = ['Anne', 'Micha', 'Sandra', 'Stefan', 'Tilman']
beschenktenamen = list(schenkernamen)
sicherheit = list(schenkernamen)
wichtelpartner, erfolgreich = [], 0

while erfolgreich == 0:
	fehler = 0
	schenkernamen = list(sicherheit)
	beschenktenamen = list(sicherheit)
	for name in schenkernamen:
		runde = [x for x in beschenktenamen if x != name] # nicht sich selbst ziehen
		try: 
			partner = random.choice(runde)
		except:
			fehler = 1
			print "❌  Ein fehlgeschlagener Versuch."
			wichtelpartner = []
		else:
			fehler = 0
			wichtelpartner.append((schenkernamen.index(name), (schenkernamen.index(partner))))
			beschenktenamen.pop(beschenktenamen.index(partner))
	if fehler == 0: # wenn es nicht aufgeht neu ziehen
		erfolgreich = 1

for partnerschaft in wichtelpartner:
	print "🎁  ", schenkernamen[partnerschaft[0]], 'beschenkt', schenkernamen[partnerschaft[1]] + '.'
