import requests
from bs4 import BeautifulSoup
import re
import json

LIGUES_TO_ID = {
    #"premier league": "46",
     "la liga": "16108",
     "bundesliga": "43"
    # "seria a": "42"
}

BASE_URL = "https://sports.bwin.com/en/sports/indexmultileague"

def ligue_parse_html(url):
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


def ligues_url(ligue):
    return LIGUES_TO_ID.get(ligue)


def re_stake(stake):
    stake_word = re.findall(r"([\d.]*\d+)", stake)
    return stake_word


def league(soup):
    leagues = [ (re.findall(r'[a-z,A-Z]{2,20}', i.text)) for i in soup.find_all(
            'a',
            {'class': "marketboard-event-group__header-league-link marketboard-event-group__header-league-link--1"})]
    print(leagues)

def match_hour(soup, bets):
    all_hours = soup.find_all('div', {'class': "marketboard-event-without-header__market-time"})
    for i in range(len(all_hours)):
        bets[i]['date'] = {
            'day': 'X',
            'hour': all_hours[i].text
        }

def match_day(soup, bets):
    numbers = []
    dates = []
    number_of_match_in_same_day = soup.find_all('div', {
        'class': "marketboard-event-group__item-container marketboard-event-group__item-container--level-3"})
    for i in range(len(number_of_match_in_same_day)):
        number = number_of_match_in_same_day[i].find_all('div', {'class': "marketboard-event-group__item--event"})
        numbers.append(len(number))
    for i in soup.find_all('span', {
        'class': "marketboard-event-group__header-content marketboard-event-group__header-content--level-3"}):
        dates.append(i.text)
    for x in range(len(dates)):
        formatted_date = dates[x].replace("/", "-")
        formatted_date = re.findall(r'\d+[-]\d+[-]\d+', formatted_date)
        dates[x] = formatted_date
    y = 0
    x = 0
    for i in range(len(bets)):
        bets[i]['date']['day'] = dates[y]
        x += 1
        if x == numbers[y]:
            y += 1
            x = 0


def local_bets(soup):
    result = soup.find_all(
        'div', {'class': "marketboard-event-group__item-container marketboard-event-group__item-container--level-2"})
    bets = []
    for i in range(len(result)):
        bet_rows = result[i].find_all('tr', {'class': "marketboard-options-row marketboard-options-row--3-way"})
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
            bets.append(bet)
    return bets


def dicts_to_json(bets):
    with open("bwin.json", "w") as outfile:
        json.dump(bets, outfile, indent=4)


if __name__ == '__main__':
    soup = ligue_parse_html(BASE_URL)
    league(soup)
    bets = local_bets(soup)
    match_hour(soup, bets)
    match_day(soup, bets)
    dicts_to_json(bets)
    print(bets)
    print(len(bets))

    ##############################
    #   TODO
    #   zrobic w selenium clicka co otworzy tabele z zespolami
    #   przypisac ligi zespolom
    #   poprawic ew bledy w kodzie
    ##############################
