#! /usr/bin/python3
""" The Shebang (#!) characters must be placed 
at the beginning of a script."""

import cgitb
cgitb.enable()

import cgi
import athletemodel
import yate

form_data = cgi.FieldStorage()
#athlete_name = form_data['which_athlete'].value
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

print(yate.start_response())
print(yate.include_header("NUAC's Timing Data"))
print(yate.header("Athlete: " + athlete['Name'] + ", DOB: " + athlete['DOB'] + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete['top3']))
print(yate.para("The entire set of timing data is: " + str(athlete['data']) + " (duplicates removed)."))
print(yate.include_footer({"Home" : "/index.html", "Select another athele" : "generate_list.py"}))
