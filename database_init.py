import sqlite3

conn = sqlite3.connect('sg_transport.db')
cursor = conn.cursor()
conn.execute('''
CREATE TABLE IF NOT EXISTS busstop(
BusStopCode TEXT PRIMARY KEY UNIQUE NOT NULL,
RoadName TEXT NOT NULL,
Description TEXT NOT NULL,
Latitude REAL NOT NULL,
LONGITUDE REAL NOT NULL
)''')
conn.commit()

conn.close()