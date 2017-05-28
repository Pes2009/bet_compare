import json

NAMES_BACKENDS = ['sts', 'bwin']


def load_jsons(list_of_backends):
    backends = {}
    for backend in list_of_backends:
        full_name = backend + ".json"
        with open(full_name) as json_data:
            json_backend = json.load(json_data)
            backends[backend] = json_backend
    return backends


def print_leagues(backends):
    for backend in backends.get('sts', 'backend not found'):
        print("{} - {}".format(backend.get('meta').get('home'),
                               backend.get('meta').get('away')))


def print_stake(STS_STAKE, BWIN_STAKE):
    print("STS stake {}".format(STS_STAKE))
    print("BWIN stake {}".format(BWIN_STAKE))


def search_team_name_in_backends(backends):
    STS_STAKE = 1.0 
    BWIN_STAKE = 1.0
    while True:
        try:
            first_team_name, second_team_name = input("podaj nazwy zespolow").split()
            break
        except ValueError:
            print("nie podales dwoch nazw")
    for i in backends:
        for backend in backends.get(i, 'backend not found'):
            if first_team_name in backend.get('meta').get('home') \
                    and second_team_name in backend.get('meta').get('away'):
                print("buchmaker {}".format(i))
                print("|  1  |  X  |  2 |")
                print("|{} |{} |{}|".format(backend.get('1').get('odds'),
                                            backend.get('X').get('odds'),
                                            backend.get('2').get('odds')))
                if i == 'sts':
                    sts = backend
                else:
                    bwin = backend

    choice = input("wybierz 1, X, 2")
    sts_odds = float(sts.get(choice).get('odds'))
    bwin_odds = float(bwin.get(choice).get('odds'))
    STS_STAKE *= sts_odds
    BWIN_STAKE *= bwin_odds
    print_stake(STS_STAKE, BWIN_STAKE)


def program_kernel():
    while True:
        try:
            display_option = int(input("1) wyswietl mecze\n"
                                       "2) obstaw mecz\n"
                                       "3) wyjdz\n"))
        except ValueError:
            # assert z in y, "input should be 1,2 or 3"
            print("Tylko liczby")

        else:
            if display_option == 1:
                print_leagues(backends)
            elif display_option == 2:
                search_team_name_in_backends(backends)
            elif display_option == 3:
                break
            else:
                print("zly wybor")


if __name__ == '__main__':
    backends = load_jsons(NAMES_BACKENDS)
    program_kernel()
    ################################################
    #   zoptymalizować kod oraz excepty            #
    #   zrobic porzadnie funkcje print leagues,    #
    #   zeby wyswietlalo tylko jak sa mecze,       #
    #   w obu bukach.                              #
    ################################################
