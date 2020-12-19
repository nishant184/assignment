
  

#Get input from the user for no: of rounds
rounds = int(input("No of rounds to play "))

#setting scores values
scores={"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}

check_bonus=[]
player_bonus=[]

# Given the players list w r t its team with  initial score zero

teams={"Gyrhuna":[{"Jaons Dain":0},{"Susu":0}],
       "Achni":[{"Milog":0},{"Tianlong":0}],
       "Bathar":[{"Pakhangba":0},{"Poubi Lai Paphal":0}]}

teamno=len(teams)
team_bonus={}
teamscore={}
def teamwon(teamscore):
    return [key  for (key, value) in teamscore.items() if value == max(teamscore.values()) if value <= 60]


for team in teams:
    team_bonus[team]=0
    teamscore[team]=0
players=0
for i in teams:
    players+=len(teams[i])


p_scores={}

for r in range(rounds):
    for team in teams:

        check_bonus=[]
        player_bonus=[]
        teamscore[team]=0
        for pl in teams[team]:
            key, value = list(pl.items())[0]
            temp=0
            p_score=(input("Enter the score of " +str(key)+str(" from team ")+team+" "))
            if p_score not in (["A","B","C","D","E","F"]):
                print("Please select the score from A-F")
            check_bonus.append(p_score)
            player_bonus.append(key)
            x=key
            if x  not in  p_scores:

                p_scores[x]=scores[p_score]
                #print(p_scores[x])
            else:
                p_scores[x]+=scores[p_score]
                temp=p_scores[x]
            teamscore[team]+=p_scores[x]

        if(len(set(check_bonus))==1):
            #print("has bonus")
            team_bonus[team]+=2
        teamscore[team]+=team_bonus[team]

    scores={key:value+1 if(key!="F") else value  for key,value in(scores.items()) }

    print(p_scores)
    print(team_bonus)
    print(teamscore)
    print("Next Round")

def teamwon(teamscore):
    return [key  for (key, value) in teamscore.items() if value == max(teamscore.values()) if value <= 60]


key=teamwon(teamscore)[0]
print("Tournament won by  {}!! ".format(key))
