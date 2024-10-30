import json
import sys

MD5SBH = sys.argv[1]

S = "U2FsdGVkX18LCdwBUA2QJ9i1B2NBOmREi2WSKGH5xA4="
A = "U2FsdGVkX1/57Xx2ss7Cban6+GthY/DFJbRvF1JJd5g="
B = "U2FsdGVkX1/Um3+YVc7NtbcuwcN1bEgaFXwP/hyQyn0="
C = "U2FsdGVkX18gJOfuAISIDhsxlvL2uB//jhZMZ0L/JCA="
D = "U2FsdGVkX1/gGnzGXgViXkbNRJHjDIiPgKsBg0y01w8="

id_No = str(input("{id}を入力してください。:"))
img_souce = str(input("{img}を入力してください。:"))
x = str(input("{rank}を入力してください。(S,A,B,C,D):"))
if x == 'S' :
 rank_code = S
elif x == 'A' :
 rank_code = A
elif x == 'B' :
 rank_code = B
elif x == 'C' :
 rank_code = C
elif x == 'D' :
 rank_code = D
stock_have = str(input("{stock}を入力してください。:"))
#BlockChainhash_of_img = str(input("{BlockChainhash}を入力してください。:"))
serial_No = str(input("{serial}を入力してください。:"))

def write_json(new_student, filename="./Product_IMG.json"):
    with open(filename, "r+") as file:
        file_content = json.load(file)
        file_content.append(new_student)
        file.seek(0)
        json.dump(file_content, file, indent=4)


new_student = {
    "id": id_No,
    "img": img_souce,
    "rank": rank_code,
    "stock": stock_have,
    "BlockChainhash": MD5SBH,
    "serial": serial_No
}

write_json(new_student)