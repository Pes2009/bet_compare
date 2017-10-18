import json

import requests
from bs4 import BeautifulSoup

country_league = (
    ['niemcy', 'bundesliga'], ["hiszpania", "laliga"], ["francja", "ligue-1"], ["anglia", "premier-league"],
    ["polska", "ekstraklasa"], ["wlochy", "serie-a"])


def urle(args):
    start = "https://www.flashscore.pl/pilka-nozna/"
    end = "/zespoly/"
    uerele = [start + args[i][0] + "/" + args[i][1] + end for i in range(len(args))]
    print(uerele)
    return uerele


def ligue_parse_html(url):
    soups = []
    for i in range(len(url)):
        r = requests.get(url[i])
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        soups.append(soup)
    return soups


def league(soups, country_league):
    sorted_teams_in_leagues = [
         {"kraj": country_league[ii][0],
          "liga": country_league[ii][1],
          "zespoly": [i.text for i in soups[ii].find_all('tr', {'odd', 'even'})]
         } for ii in range(len(soups))]
    return sorted_teams_in_leagues

def dicts_to_json(bets):
    with open("sorted_teams.json", "w") as outfile:
        json.dump(bets, outfile, indent=4)


if __name__ == '__main__':
    x = urle(country_league)
    soup = ligue_parse_html(x)
    save = league(soup, country_league)
    dicts_to_json(save)
