import requests
import json
import sqlite3

# conn = sqlite3.connect("PC_Store_DB.db")
# curr = conn.cursor()
# print(curr.execute('''delete from PC where pc_ID = 2
#     ''').fetchall())
# conn.commit()
# conn.close()

# data = requests.post("http://127.0.0.1:5000/", data={'data': json.dumps([1, "Esqin", "Hasanov", "esqin@gmail.com", 2])}).json()
# data = requests.post("http://127.0.0.1:5000/add_pc", data={'data': json.dumps([1, "ryzen7", 16, "sata 512", 900])}).json()
data = requests.delete("http://127.0.0.1:5000/remove_pc/1").json()
print(data)