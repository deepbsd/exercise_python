import re

def tally(tournament_results):
    header = "Team                           | MP |  W |  D |  L |  P\n"

    teams = {
            'Allegoric Alaskans': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            'Blithering Badgers': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            'Devastating Donkeys': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            'Courageous Californians': {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0},
            }

    table = header

    output = []

    lines = tournament_results.split("\n")

    for line in lines:
        if not line: break
        m = re.search('(.*);(.*);(.*)\n?',line)
        team1 = m.group(1); team2 = m.group(2); outcome = m.group(3)
        if outcome == "win":
            teams[team1]['MP'] += 1; teams[team1]['W'] += 1; teams[team1]['P'] += 3
            teams[team2]['MP'] += 1; teams[team2]['L'] += 1; 
        if outcome == "loss":
            teams[team1]['MP'] += 1; teams[team1]['L'] += 1; 
            teams[team2]['MP'] += 1; teams[team2]['W'] += 1; teams[team2]['P'] += 3
        if outcome == "draw":
            teams[team1]['MP'] += 1; teams[team1]['D'] += 1; teams[team1]['P'] += 1
            teams[team2]['MP'] += 1; teams[team2]['D'] += 1; teams[team2]['P'] += 1

    #for team, val in teams.items():
    #    for k,v in val.items():
    #        if k == "P": print(team,' points: ',v)

    for key, team in teams.items():
        if team['MP']: table += "{:<30s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s}\n".format(key, team['MP'], team['W'], team['D'], team['L'], team['P'])

        if team['MP']: output.append("{:<30s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s}\n".format(key, team['MP'], team['W'], team['D'], team['L'], team['P']))
        


    output[-1] = output[-1].rstrip("\n")
    for line in output:
        print(line)
    
    table = table.rstrip("\n")
    #return table
    return table




if __name__ == "__main__":
    print(tally('Blithering Badgers;Allegoric Alaskans;draw'))
