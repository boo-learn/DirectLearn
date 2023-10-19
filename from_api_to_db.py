import requests
import json
import sqlite3
from settings import TOKEN, urls


def get_data_from_api():
    headers = {
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json"
    }

    body = {
        "method": "get",
        "params": {
            "FieldNames": ["Id", "Name", "Type", "State", "Status"],
            "SelectionCriteria": {
                # "Types": ["SMART_CAMPAIGN"],
                # "Statuses": ["DRAFT", "ACCEPTED"]
            },
            # "Page": {
            #     "Limit": 10,
            #     "Offset": 20
            # }
        }
    }

    response = requests.post(urls['campaigns'], data=json.dumps(body), headers=headers)
    return response.json()


def create_tables():
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
    con.close()


def save_to_db(data: list[dict]):
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    data_tupes = []
    for comp in data:
        data_tupes.append(tuple(comp.values()))
    cur.executemany("INSERT INTO Campaigns VALUES(?, ?, ?, ?, ?)", data_tupes)
    con.commit()
    con.close()


def read_from_db():
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    res = cur.execute("""
    SELECT * FROM Campaigns;
    """)
    return res.fetchall()

# result = get_data_from_api()
# campains = result['result']['Campaigns']
# create_tables()
# save_to_db(campains)

res = read_from_db()
print(res)
