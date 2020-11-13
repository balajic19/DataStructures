'''
Football tournament

win - 3 points
draw - 1 point
lose - 0 points

Input:
N = 3 (number of teams)
A B 2-1
B C 2-1
C A 1-2

Output:
A (team)
6 (points)
'''

class Tournament():
    def __init__(self):
        return

    def find_winner(self, dic):
        return max(dic, key = dic.get) 



n = int(input("Enter N: "))

comb = (n * (n-1))//2
dic = {}
for i in range(comb):
    scoreCard = input()
    obj = Tournament()
    team1 = scoreCard.split()[0]
    team2 = scoreCard.split()[1]
    score = scoreCard.split()[2]
    score1 = score.split('-')[0]
    score2 = score.split('-')[1]\

    if str(team1) not in dic.keys():
        dic[str(team1)] = 0
    if str(team2) not in dic.keys():
        dic[str(team2)] = 0
    

    if score1 > score2:
        dic[str(team1)] += 3
    elif score1 < score2:
        dic[str(team2)] += 3
    else:
        dic[str(team1)] += 1
        dic[str(team2)] += 1
winner = obj.find_winner(dic)
print(winner)
print(dic[winner])

