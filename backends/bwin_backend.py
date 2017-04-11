import requests
from bs4 import BeautifulSoup
import re
import json

LIGUES_TO_ID = {
    "premier league": "46",
    "la liga": "16108",
    "bundesliga": "43",
    "seria a": "42"
}

BASE_URL = "https://sports.bwin.com/en/sports/indexmultileague"


def get_ligue_parse_html(url):
    r = requests.post(
        url,
        data={
            'sportId': '4',
            'page': '0',
            'leagueIds': [LIGUES_TO_ID.values()]
        })
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    return soup


def get_ligue_url(ligue):
    return LIGUES_TO_ID.get(ligue)


def re_stake(stake):
    stake_word = re.findall(r"([\d.]*\d+)", stake)
    return stake_word


def get_local_bets(soup):
    result = soup.find_all(
        'div', {'class': "marketboard-event-group__item-container marketboard-event-group__item-container--level-2"})
    bets = []
    hour = []
    number_teams_on_date_match_in_seq = []
    # for date_match in soup.find_all(
    #     'span', {'class': "marketboard-event-group__header-content marketboard-event-group__header-content--level-3"}):
    #     print(date_match.text)
    #
    #
    # number_of_date_match_on_page = soup.find_all(
    #     'div', {'class': "marketboard-event-group__item-container marketboard-event-group__item-container--level-3"})
    # print(len(number_of_date_match_on_page))
    # for i in soup.find_all('div', {
    #     'class': "marketboard-event-group__item-container marketboard-event-group__item-container--level-3"}):
    #     number_teams_on_this_same_date = (len(i) - 1) / 2
    #     number_teams_on_date_match_in_seq.append(int(number_teams_on_this_same_date))
    for i in range(len(result)):
        bet_rows = result[i].find_all('tr', {'class': "marketboard-options-row marketboard-options-row--3-way"})
        for link in soup.find_all('div', {'class': "marketboard-event-without-header__market-time"}):
            hour.append(link.text)
        for row in bet_rows:
            choices = row.select('.mb-option-button__option-name')
            odds = row.select('.mb-option-button__option-odds')
            bet = {
                symbol: {
                    'team': choices[i].text,
                    'odds': odds[i].text,
                }
                for i, symbol in enumerate(['1', 'X', '2'])
            }
            bet['meta'] = {
                'home': choices[0].text,
                'away': choices[2].text
            }
            for i in range(len(hour)):
                bet['date'] = {
                    'day': 'X',
                    'hour': hour[i]
                }
            bets.append(bet)
    return bets


def dicts_to_json(bets):
    with open("bwin.json", "w") as outfile:
        json.dump(bets, outfile, indent=4)


if __name__ == '__main__':
    soup = get_ligue_parse_html(BASE_URL)
    bets = get_local_bets(soup)
    dicts_to_json(bets)
    print(bets)
print(len(bets))

##############################
#   TODO
#   MAKE DAY DATE IN BET DICTS
##############################