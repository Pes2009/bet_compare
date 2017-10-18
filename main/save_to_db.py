import json
import pymongo
from pymongo import MongoClient
def read_json(data):
    with open(data) as data_file:
        data = json.load(data_file)
        return data
client = MongoClient('localhost', 27017)
db = client.bet_compare

NAMES_BACKENDS = ['sts', 'bwin']
sorted_teams = read_json('sorted_teams.json')
bwin_json = read_json('bwin.json')
sts_json = read_json('sts.json')

name_teams_tuple = [
    ('FC Augsburg', "Augsburg"),
    ('FC Bayern Munich', "Bayern"),
    ('Werder Bremen', "Bremen"),
    ('Borussia Dortmund', "Dortmund"),
    ('1. FC Köln', "FC Koln"),
    ('Eintracht Frankfurt', "Frankfurt"),
    ('SC Freiburg', "Freiburg"),
    ('Hamburger SV', "Hamburger SV"),
    ('Hannover 96', "Hannover"),
    ('Hertha BSC', "Hertha"),
    ('1899 Hoffenheim', "Hoffenheim"),
    ("Bayer Leverkusen", "Leverkusen"),
    ('FSV Mainz 05', "Mainz"),
    ('Borussia Mönchengladbach', "Monchengladbach"),
    ('RasenBallsport Leipzig', "RB Lipsk"),
    ("FC Schalke 04", "Schalke"),
    ('VfB Stuttgart', "Stuttgart"),
    ('VfL Wolfsburg', "Wolfsburg"),
    ('Espanyol', "Espanyol"),
    ('Real Madrid', "Real Madryt"),
    ('Atletico Madrid', "Atl. Madryt"),
    ('FC Sevilla', "Sevilla"),
    ('Getafe', "Getafe"),
    ('Deportivo Alaves', "Alaves"),
    ('Real Sociedad', "Real Sociedad"),
    ('FC Barcelona', "Barcelona"),
    ('Athletic Club', "Ath. Bilbao"),
    ('Real Betis', "Betis"),
    ('Celta de Vigo', "Celta Vigo"),
    ('SD Eibar', "Eibar"),
    ('Girona', "Girona"),
    ('UD Las Palmas', "Las Palmas"),
    ('Deportivo La Coruna', "La Coruna"),
    ('Leganes', "Leganes"),
    ('Malaga', "Malaga"),
    ('CF Valencia', "Valencia"),
    ('Villarreal', "Villarreal")

]


def load_jsons(list_of_backends):
    backends = {}
    for backend in list_of_backends:
        full_name = backend + ".json"
        with open(full_name) as json_data:
            json_backend = json.load(json_data)
            backends[backend] = json_backend
    return backends


def poprawne_nazwy_zespolo(name_teams_tuple, finall_names):
    for i in backends:
        for backend in backends.get(i, 'backend not found'):
            for i in name_teams_tuple:
                if backend['meta']['home'] in i[0]:
                    backend['meta']['home'] = i[1]
                    for c in finall_names:
                        if backend['meta']['home'] in c['zespoly']:
                            backend['meta']['country'] = c['kraj']
                            backend['meta']['ligue'] = c['liga']
                if backend['meta']['away'] in i[0]:
                    backend['meta']['away'] = i[1]
                    for c in finall_names:
                        if backend['meta']['home'] in c:
                            backend['meta']['country'] = c['kraj']
                            backend['meta']['ligue'] = c['liga']


if __name__ == '__main__':
    backends = load_jsons(NAMES_BACKENDS)
    poprawne_nazwy_zespolo(name_teams_tuple, sorted_teams)
    # for i in backends:
    #     for row in backends.get(i):
    #         result = db.bets.insert_one(row)
    cursor = db.bets.find()
    for document in cursor:
            print(document)
