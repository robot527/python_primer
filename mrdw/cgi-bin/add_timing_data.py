#! /usr/bin/python3

#import cgitb
#cgitb.enable()

import cgi
import sqlite3
import yate

print(yate.start_response('text/plain'))

form = cgi.FieldStorage()

new_data = {}
for key in form.keys():
	new_data[key] = form[key].value
#print(new_data)
the_id = new_data['Athlete_id']
the_time = new_data['Time']
#print(the_id, the_time)

db = './cgi-bin/coachdata.sqlite'
connection = sqlite3.connect(db)
cursor = connection.cursor()
cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES(?, ?)",
		(the_id, the_time))

connection.commit()
connection.close()

print('Insert new data into ' + db + ' OK.')
