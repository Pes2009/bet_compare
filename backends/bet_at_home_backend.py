import json
import re
import requests
from bs4 import BeautifulSoup
LIGUES_TO_ID = {
'sport': '184',
        'region': '6482',
        'league': '4079',
        'action': 'offer',
    }
BASE_URL = "https://www.sts.pl/pl/oferta/zaklady-bukmacherskie/zaklady-sportowe/?action=offer"



def get_ligue_parse_html(url):
    r = requests.post(
        url,
        data=LIGUES_TO_ID)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    return soup


def get_ligue_url(ligue):
    return LIGUES_TO_ID.get(ligue)


def get_local_bets(soup):
    result = soup.find_all(
        'div', {'class': "shadow_box support_bets_offer"})
    bets = []
    bets_x = []
    for i in range(len(result)):
        for link2 in soup.find_all('td', {'class': 'bet smallTip'}):
            odds = link2.find('a').span.text
            bets_x.append(odds)
        for row in soup.find_all('td', {'class': "bet bigTip"}):
            choices = row.find('a').contents[0]
            m = re.findall(r"[A-Za-z]+", choices)
            print(m)
            choices = m.pop()
            odds = row.find('a').span.text
            bet = {

                'team': choices,
                'odds': odds,
            }
            bets.append(bet)
    bets.append(bets_x)
    return bets

def serialize_dictionary(bets):
    bets_x = bets.pop()
    bets_x.reverse()
    final_bets = []
    size = len(bets)
    for i in range(size):
        if i % 2 == 0:
            bet = {
                '1': {

                    'team': bets[i].get('team'),
                    'odds': bets[i].get('odds'),
                }
            }
        else:
            bet['2'] = {
                'team': bets[i].get('team'),
                'odds': bets[i].get('odds'),
            }
            bet['X'] = {
                'team': 'X',
                'odds': bets_x.pop()
            }
            bet['meta'] = {
                'home': bet['1'].get('team'),
                'away': bet['2'].get('team')
            }
            final_bets.append(bet)
    return final_bets


def dicts_to_json(bets):
    with open("sts.json", "w") as outfile:
        json.dump(bets, outfile, indent=4)

if __name__ == '__main__':
    soup = get_ligue_parse_html(BASE_URL)
    bets = get_local_bets(soup)
    print(bets)
    x = serialize_dictionary(bets)
    dicts_to_json(x)

##############################
#   TODO
#   MAKE DAY DATE IN BET DICTS
##############################