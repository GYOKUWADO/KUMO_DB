import json

json_open = open('./Product_IMG.json', 'r')
json_load = json.load(json_open)

S = "U2FsdGVkX18LCdwBUA2QJ9i1B2NBOmREi2WSKGH5xA4="
A = "U2FsdGVkX1/57Xx2ss7Cban6+GthY/DFJbRvF1JJd5g="
B = "U2FsdGVkX1/Um3+YVc7NtbcuwcN1bEgaFXwP/hyQyn0="
C = "U2FsdGVkX18gJOfuAISIDhsxlvL2uB//jhZMZ0L/JCA="
D = "U2FsdGVkX1/gGnzGXgViXkbNRJHjDIiPgKsBg0y01w8="

id = str(input("[S][A][B][C][D]のランクを選択してください。:"))

print("id  stock[0:don't have][1:have]")

for d in json_load:

    res_a = d['id']
    res_b = d['img']
    res_c = d['rank']
    res_d = d['stock']

    #if id == res_c:
    #   print(res_a + " " + res_d)

    if id == "S":
       if res_c == S:
          print(res_a + " " + res_d)
    if id == "A":
       if res_c == A:
          print(res_a + " " + res_d)
    if id == "B":
       if res_c == B:
          print(res_a + " " + res_d)
    if id == "C":
       if res_c == C:
          print(res_a + " " + res_d)
    if id == "D":
       if res_c == D:
          print(res_a + " " + res_d)