import sqlite3

con = sqlite3.connect("example.db")

cur = con.cursor()

res = cur.execute("""
SELECT * FROM Campaigns;
""")

data = res.fetchall()
print(f"{data=}")