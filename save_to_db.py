import sqlite3

con = sqlite3.connect("example.db")

cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Campaigns (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name TEXT NOT NULL,
  State TEXT NOT NULL,
  Status TEXT NOT NULL,
  Type TEXT NOT NULL
)
""")

cur.execute("""
INSERT INTO Campaigns (Name, State, Status, Type)
VALUES 
('Test Company', 'OFF', 'ACCEPTED', 'TEXT_CAMPAIGN'),
('Test Company 2', 'OFF', 'ACCEPTED', 'TEXT_CAMPAIGN'),
('Test Company 3', 'OFF', 'ACCEPTED', 'TEXT_CAMPAIGN');
            """)
con.commit()
