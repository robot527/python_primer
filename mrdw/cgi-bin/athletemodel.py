import sqlite3

db_name = 'coachdata.sqlite'

def get_names_from_store():
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	results = cursor.execute("""SELECT name FROM athletes""") #extract the data
	response = [row[0] for row in results.fetchall()] #formulate a list
	connection.close()
	return (response)

#Gets the data asscoiated with a specific ID
def get_athlete_from_id(athlete_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	#get the "name" and "DOB" values from the athletes table
	results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""",(athlete_id,))
	(name, dob) = results.fetchone()
	#get the list of times from the timing_data table
	results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""",   (athlete_id,))
	data = [row[0] for row in results.fetchall()]
	data.sort()
	#take the data from both query results and turn it into a dictionary
	response = {	'Name': name, 
			'DOB': dob,
			'data': data,
			'top3': data[0:3]}
	connection.close()
	return (response)

def get_namesID_from_store():
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	results = cursor.execute("""SELECT name, id FROM athletes""")
	response = results.fetchall()
	connection.close()
	return (response)

def check_athleteId(athlete_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	results = cursor.execute("""SELECT name FROM athletes WHERE id = ?""", (athlete_id,))
	sel_data = results.fetchall()
	connection.close()
	if sel_data == []:
		return (False)
	else:
		return (True)
