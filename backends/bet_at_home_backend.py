import requests
from bs4 import BeautifulSoup



BASE_URL = "https://www.sts.pl/pl/oferta/zaklady-bukmacherskie/zaklady-sportowe/?action=offer"


r = requests.get(BASE_URL)

r = requests.post(
    "https://www.sts.pl/pl/oferta/zaklady-bukmacherskie/zaklady-sportowe/",
        data={
            'sport': '184',
            'region': '6502',
            'leagueIds': '4163'
        })
data = r.text

soup = BeautifulSoup(data, "html.parser")

def get_local_bets(soup):
    result = soup.find_all(
        'div', {'class': "shadow_box support_bets_offer"})
    # print(result)
    bets = []
    for z in range(len(result)):
        bet_rows = result[z].find_all('table', {'class': "col3"})
        # print(bet_rows)
        # for link in soup.find_all('table', {'class': "subTable"}):
        #     #print(link.text)
        #     print(link.text)
        #     # print(link.span.text)
        #     print("spacja")
        # x = result[z].find_all('table', {'class': "subTable"})



    return bets

get_local_bets(soup)

#print(soup.prettify())


######################
#   IN BUILD
######################