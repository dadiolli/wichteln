# -*- coding: utf-8 -*-
from app import app
from .newgroup import NewGroup
from .obscure import encode, decode
#from .algorithm import wichteln
from flask import flash, redirect, render_template, request
import csv, os.path, random, socket, sys, time

# need to reload sys to set default encoding
reload(sys)
sys.setdefaultencoding('utf-8')

csv_source = 'app/groups/' + 'wichtelgruppen.csv'

@app.route('/')
@app.route('/index')

def wichteln():
	user = {'nickname': 'Anonyme Benutzerin'}
	navbar = {'newgroup': '',
			  'index': 'active',
			  'other': ''}
	if request.args.get('key'):
		key = request.args.get('key', type = str)
		session = key[0:15]
		passphrase = key[15:]
		user = {'nickname': decode(passphrase)}
		#load data from the css
		reader = csv.reader(open(csv_source, 'r'), delimiter = ';')
		d = {}
		for row in reader:
			d[(row[0], row[1])] = row[2]
		partner = decode(d[(session, passphrase)])
		return render_template('index.html', title='Wichtelgruppe', user=user, navbar=navbar, secret=partner)
	else:
		return render_template('index.html', title='Startseite', user=user, navbar=navbar)

@app.route('/newgroup', methods=['GET', 'POST'])
def newgroup():
	navbar = {'newgroup': 'active', 'index': '', 'other': ''}
	form = NewGroup()
	if form.validate_on_submit():
		if ',' in form.namesfield.data:
			form.namesfield.data = form.namesfield.data.replace(', ',',')
			allenamen = form.namesfield.data.split(',')
			duplikate = [name for name in allenamen if allenamen.count(name) > 1]
			if len(duplikate) > 0:
				return render_template('newgroup.html', navbar=navbar, title='Neue Wichtelgruppe anlegen', form=form,
										error='Jede Person darf nur einmal vorkommen.')
			namelist = ', '.join(allenamen[:-1]) + " und " + allenamen[-1]
			result, keylist, count = [], [], 1
			allenamen = tuple(allenamen)
			eins, zwei, zyklus = range(len(allenamen)), range(len(allenamen)), 1
			while zyklus > 0:
				random.shuffle(eins)
				random.shuffle(zwei)
				zyklus = len([i for i, j in zip(eins, zwei) if i == j])
			session = time.strftime("%Y%m%d-%H%M%S")
			for schenker in eins:
				result.append((session, encode(allenamen[schenker]), encode(allenamen[zwei[eins.index(schenker)]])))
				#result += u"🎁 " + allenamen[schenker] + " beschenkt " + allenamen[zwei[eins.index(schenker)]] + ".\n"
				keylist.append((count, allenamen[schenker], session, encode(allenamen[schenker])))
				count += 1
			csv.register_dialect('yeti', delimiter = ';', skipinitialspace = 1, quoting = csv.QUOTE_MINIMAL, quotechar = '"', lineterminator = '\n')
			if not os.path.isfile('app/groups/wichtelgruppen.csv'):
				with open(csv_source, 'wb') as f:
					f.write(u'\ufeff')
					writer = csv.writer(f, dialect='yeti')
					writer.writerow(('key','schenkerin','beschenkte'))
			with open(csv_source, 'a') as f:
				writer = csv.writer(f, dialect='yeti')
				writer.writerows(result)
			return render_template('success.html', namelist=namelist, navbar=navbar, results=keylist, title='Neue Wichtelgruppe angelegt.', urlstart=request.url_root)
		else:
			return render_template('newgroup.html', navbar=navbar, title='Neue Wichtelgruppe anlegen', form=form,
									error='Deine Eingabe war leider nicht geschickt.')
	return render_template('newgroup.html', navbar=navbar, title='Neue Wichtelgruppe anlegen', form=form)