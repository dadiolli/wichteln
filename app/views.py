# -*- coding: utf-8 -*-
from app import app
from .newgroup import NewGroup
from flask import render_template
import random

@app.route('/')
@app.route('/index')

def wichteln():
	user = {'nickname': 'Anonyme Benutzerin'}
	result = ''
	allenamen = ('Anne', 'Micha', 'Sandra', 'Stefan', 'Tilman')
	eins, zwei, zyklus = range(len(allenamen)), range(len(allenamen)), 1
	while zyklus > 0:
		random.shuffle(eins)
		random.shuffle(zwei)
		zyklus = len([i for i, j in zip(eins, zwei) if i == j])
	for schenker in eins:
		result += "🎁 " + allenamen[schenker] + " beschenkt " + allenamen[zwei[eins.index(schenker)]] + ".<br/>"
	return render_template('index.html', title='Startseite', user=user)

@app.route('/newgroup', methods=['GET', 'POST'])
def newgroup():
    form = NewGroup()
    return render_template('newgroup.html', 
                           title='Neue Wichtelgruppe anlegen',
                           form=form)