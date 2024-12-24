import time
import csv
import requests

file = open("touhous.txt", "r", encoding='utf-8')
names = file.readlines()

tag_url = "https://danbooru.donmai.us/counts/posts.json?tags="

output = open("census.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(output)
writer.writerow(["name","total", "solo_count", "lonely(%)","wholesome_count","wholesome(%)","lewd_count","lewd(%)","ship_count","ship(%)","kink_count","kink(%)"])
print("Getting post counts:")
for name in names:
    response = requests.get(tag_url+name.strip(),headers={"User-Agent": "touhou-census/testing"})
    char_count = response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"solo",headers={"User-Agent": "touhou-census/testing"})
    solo_count = response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"rating:general",headers={"User-Agent": "touhou-census/testing"})
    wholesome_count = response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"rating:explicit",headers={"User-Agent": "touhou-census/testing"})
    lewd_count = response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"yuri",headers={"User-Agent": "touhou-census/testing"})
    yuri_count = response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"bondage",headers={"User-Agent": "touhou-census/testing"})
    kink_count = response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"exhibitionism",headers={"User-Agent": "touhou-census/testing"})
    kink_count += response.json()['counts']['posts']

    response = requests.get(tag_url+name.strip()+"+"+"tentacles",headers={"User-Agent": "touhou-census/testing"})
    kink_count += response.json()['counts']['posts']

    kink = round((kink_count/char_count)*100,2)
    yuri = round((yuri_count/char_count)*100,2)
    lewd = round((lewd_count/char_count)*100,2)
    lonely = round((solo_count/char_count)*100,2)
    wholesome = round((wholesome_count/char_count)*100,2)
    writer.writerow([name.strip(),char_count,solo_count,lonely,wholesome_count,wholesome,lewd_count,lewd,yuri_count,yuri,kink_count,kink])
    print(f"Got {name.strip()}")
    output.flush() # in case of early termination
    #time.sleep(1)