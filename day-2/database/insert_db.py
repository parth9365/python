import sqlite3
conn = sqlite3.connect('school.db')
print 'Opened database successfully'

conn.execute("INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS, STANDARD) \
	VALUES (1, 'Parth', 24, 'India', 15 ) ")

conn.execute("INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS, STANDARD) \
	VALUES (2, 'Yash', 20, 'Ahmedabad', 12) ")

conn.commit()
print "Records created successfully"
conn.close()