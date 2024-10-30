import json

json_open = open('./Product_IMG.json', 'r')
json_load = json.load(json_open)

json_open.close()

id = str(input("在庫を修正する品物のIDを入力してください。:"))
stock = str(input("在庫を入力してください:"))

for d in json_load:
    res_a = d['id']
    res_b = d['stock']
    if id == res_a:
       d['stock'] = stock
#print(json_load)
new_json = open('./Product_IMG.json', 'w')
json.dump(json_load, new_json, indent=4)