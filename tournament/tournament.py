import re

def tally(tournament_results):
    header = 'Team                           | MP |  W |  D |  L |  P'

    #stats = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

    teams = {
            'Allegoric Alaskans': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            'Blithering Badgers': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            'Devastating Donkeys': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            'Courageous Californians': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            }

    for line in tournament_results:
        print(line)
        m = re.search('(.*);(.*);(.*)',line)

    return m.group(1)




if __name__ == "__main__":
    print(tally('whatever;whoever;win'))
