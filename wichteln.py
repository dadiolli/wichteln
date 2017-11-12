# -*- coding: utf-8 -*-
from flask import Flask
import random
app = Flask(__name__)
@app.route("/")
def wichteln():
	result = ''
	allenamen = ('Anne', 'Micha', 'Sandra', 'Stefan', 'Tilman')
	eins, zwei, zyklus = range(len(allenamen)), range(len(allenamen)), 1
	while zyklus > 0:
		random.shuffle(eins)
		random.shuffle(zwei)
		zyklus = len([i for i, j in zip(eins, zwei) if i == j])
	for schenker in eins:
		result += "🎁 " + allenamen[schenker] + " beschenkt " + allenamen[zwei[eins.index(schenker)]] + ".<br/>"
	return result