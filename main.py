import random 
roles = ["Mordred","Merlin","Loyal Servant of Arthur","Loyal Servant of Arthur","Minion of Mordred"]
extra_roles = ["Loyal Servant of Arthur","Minion of Mordred","Loyal Servant of Arthur","Loyal Servant of Arthur","Minion of Mordred"]
player_names = []
turn = 0
def get_roles(players): # assign a role to each player
  player_roles = []
  if players == 10: # restrict number of roles to number of players
    possible_roles = roles + extra_roles
  else:
    possible_roles = roles + extra_roles[0:players-5]
  for player in range(players):
    role = random.choice(possible_roles)
    player_roles.append(role)
    possible_roles.remove(role)
  return player_roles # returns a list of roles to players
def play_round():
  failed_votes = 0
  round_completed = False
  while not round_completed:
    if failed_votes == 5: # evil instantly wins after 5 failed votes in a round
      round_completed = True
      return "Evil wins"
    else:
      approvers = 0
      for player in players:
        approval = input(f"{player_names[player]}, do you approve the mission, yes or no?")
        if approval.lower() == "yes":
          approvers += 1
        
    

players = int(input("Enter number of players between 5 to 10: "))
assigned_roles = get_roles(players)
for player in range(players):
  player_name = input("Enter player name: ")
  player_names.append(player_name)

for player in range(players):
  print(f"{player_names[player]} is {assigned_roles[player]}")

print("\n"*25) # prevents players from seeing each other's roles
