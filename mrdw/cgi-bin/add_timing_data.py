#! /usr/bin/python3

#import cgitb
#cgitb.enable()

import cgi
import sqlite3
import yate
from athletemodel import db_name, check_athleteId

print(yate.start_response('text/plain'))

form = cgi.FieldStorage()

new_data = {}
for key in form.keys():
	new_data[key] = form[key].value
the_id = new_data['Athlete_id']
the_time = new_data['Time']

if check_athleteId(the_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES(?, ?)", (the_id, the_time))

	connection.commit()
	connection.close()

	print('Insert new data into ' + db_name + ' OK.')
else:
	print('The id ' + the_id + ' is not in table, can not insert data!')
