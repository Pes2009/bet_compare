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


def search_team_name_in_backends(backends):
    s = 'Schalke'
    for i in backends:
        for backend in backends.get(i, 'do not found backend'):
            if s in backend.get('meta').get('away'):
                print(s)
                print(backend)
                print(str(i))


if __name__ == '__main__':
    backends = load_jsons(NAMES_BACKENDS)
    search_team_name_in_backends(backends)
