# -*- coding: utf-8 -*-
import random
allenamen = ('Anne', 'Micha', 'Sandra', 'Stefan', 'Tilman')
eins, zwei, zyklus = range(len(allenamen)), range(len(allenamen)), 1
while zyklus > 0:
	random.shuffle(eins)
	random.shuffle(zwei)
	zyklus = len([i for i, j in zip(eins, zwei) if i == j])
for schenker in eins:
	print "🎁 ", allenamen[schenker], "beschenkt", allenamen[zwei[eins.index(schenker)]] + "."
