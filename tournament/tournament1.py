
import re
from operator import itemgetter 

def tally(tournament_results):
    header = "Team                           | MP |  W |  D |  L |  P\n"

    teams = {}

    output = []

    lines = tournament_results.split("\n")

    for line in lines:
        if not line: break
        m = re.search('(.*);(.*);(.*)\n?',line)
        team1 = m.group(1); team2 = m.group(2); outcome = m.group(3)
        teams[team1] = {'MP':0, 'W':0, 'D':0, 'L':0, 'P':0}
        teams[team2] = {'MP':0, 'W':0, 'D':0, 'L':0, 'P':0}
        if outcome == "win":
            teams[team1]['MP'] += 1; teams[team1]['W'] += 1; teams[team1]['P'] += 3
            teams[team2]['MP'] += 1; teams[team2]['L'] += 1; 
        elif outcome == "loss":
            teams[team1]['MP'] += 1; teams[team1]['L'] += 1; 
            teams[team2]['MP'] += 1; teams[team2]['W'] += 1; teams[team2]['P'] += 3
        elif outcome == "draw":
            teams[team1]['MP'] += 1; teams[team1]['D'] += 1; teams[team1]['P'] += 1
            teams[team2]['MP'] += 1; teams[team2]['D'] += 1; teams[team2]['P'] += 1



    # update the values for each team and game and append to output list
    for key, team in teams.items():
        if team['MP']: output.append("{:<30s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s}".format(key, team['MP'], team['W'], team['D'], team['L'], team['P']))
        


    # Call a sort method on the list


    
    # sort the teams by total points
    for num, line in enumerate(output):
        output[num] = line[::-1]
    output = sorted(output) # , reverse=True)
    for num, line in enumerate(output):
        output[num] = line[::-1]
    


    # return the list as a string with last newline omitted
    if output: return header+"\n".join(output).rstrip("\n")
    else: return header.rstrip("\n")

    #def sort_list(teams):
    #    new_list = []
    #    for name, data in sorted(teams.items(), key = lambda team: (team[-1], team[0:5])):
    #        new_list.append(teams[name])
    #        
    #    return new_list


    #    #newdict = sorted(dict.keys(), key=lambda team: (team[0], team[1]['P']))
    #return sort_list(teams)





if __name__ == "__main__":
    print(tally('Allegoric Alaskans;Blithering Badgers;draw'))
