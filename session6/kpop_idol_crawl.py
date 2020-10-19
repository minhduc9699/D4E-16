import requests
from bs4 import BeautifulSoup

result = requests.get('https://dbkpop.com/db/all-k-pop-idols')

soup = BeautifulSoup(result.text)

table_body = soup.find('tbody')
rows = table_body.find_all('tr')

label_mapping = {
    0: 'profile_link',
    1: 'stage_name',
    2: 'full_name',
    3: 'k_name',
    4: 'k_stage_name',
    5: 'dob',
    6: 'group',
    7: 'country',
    8: 'birth_place',
    9: 'other_group',
    10: 'height',
    11: 'weight',
    12: 12,
    13: 13,
    14: 'gender',
    15: 15,
    16: 16,
    17: 17,
    18: 18
}
idols = []
for row in rows:
    idol_infos = row.find_all('td')
    idol = {}
    for i in range(len(idol_infos)):
        content = idol_infos[i].text
        idol[label_mapping[i]] = content
    idols.append(idol)
print(idols)