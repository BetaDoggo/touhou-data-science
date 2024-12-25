import time
import csv
import requests

file = open("touhous.txt", "r", encoding='utf-8')
names = file.readlines()

tag_url = "https://danbooru.donmai.us/counts/posts.json?tags="

output = open("census.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(output)

ship_list = [[""]]
for name in names:
    ship_list[0].append(name.strip())
    ship_list.append([name.strip()])

for x in range(1, len(ship_list)):
    for row in ship_list[1:]:
        row.append("")

for column in range(1, len(ship_list[1:])+1):
    for row in range(1,len(ship_list[1:])+1):
        if column != row and ship_list[column][row] == "":
            char1 = ship_list[column][0]
            char2 = ship_list[0][row]
            search = f"yuri {char1} {char2}"
            response = requests.get(tag_url+search,headers={"User-Agent": "touhou-census/testing"})
            char_count = response.json()['counts']['posts']
            print(f"{char1} X {char2}: {char_count}")
            ship_list[column][row] = char_count
            ship_list[row][column] = char_count
#print(ship_list)
for row in ship_list:
    writer.writerow(row)

