import json
from PIL import Image

json_open = open('./Product_IMG.json', 'r')
json_load = json.load(json_open)

id = str(input("品物のIDを入力してください。:"))

for d in json_load:
    res_a = d['id']
    res_b = d['img']
    if id == res_a:
       im = Image.open("./Product_IMG/" + res_b)
       im.show()