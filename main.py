import random 
roles = ["Mordred","Merlin","Loyal Servant of Arthur","Loyal Servant of Arthur","Minion of Mordred"]
extra_roles = ["Loyal Servant of Arthur","Minion of Mordred","Loyal Servant of Arthur","Loyal Servant of Arthur","Minion of Mordred"]
player_names = []
turn = 0
rounds_completed = 0
quests = {5: [2,3,2,3,3], 6: [2,3,4,3,4], 7: [2,3,3,4,4], 8: [3,4,4,5,5]}

def round_approval():
  chosen_players = []
  votes = 0
  if len(player_names) > 8:
    quest_players = 8
  else:
    quest_players = len(player_names)
  for p in range(quests[quest_players][rounds_completed]):
    person_turn = player_names[turn % len(player_names)]
    player_chosen = input(f"{person_turn}, enter someone to embark on the mission: ")
    chosen_players.append(player_chosen)
    
  print(f"The following people have been chosen: {', '.join(chosen_players)}")
  for person in range(len(player_names)):
    approval = input(f"{player_names[person]}, do you approve the mission? ")
    while approval.lower() not in ("yes","no"):
      approval = input(f"{player_names[person]}, do you approve the mission? ")
    if approval.lower() == "yes":
        votes += 1
  if votes > len(player_names) / 2:
    print("The mission has been approved!")
    return [True, chosen_players]
  else:
    print("The mission has been rejected")
    return [False]

def mission(mission_players):
  fails = 0
  for p in range(len(mission_players)):
    index = player_names.index(mission_players[p])
    if assigned_roles[index] in ("Mordred","Minion of Mordred"):
      status = input("Succeed or fail the mission: ")
      while status.lower() not in ("succeed","fail"):
        status = input("Succeed or fail the mission: ")
    else:
      status = "succeed"
    if status.lower() == "fail":
      fails += 1
    if rounds_completed == 3:
      if fails >= 2:
        print("Mission failed!")
        return False
      else:
        print("Mission succeeded!")
        return True
    else:
      if fails >= 1:
        print("Mission failed!")
        return False
      else:
        print("Mission succeeded!")
        return True
      
    
def round_player():
  global turn
  rejected_teams = 0
  mission_commenced = False
  while not mission_commenced:
    if rejected_teams == 5:
      return ("Round not played")
    mission_approval = round_approval()
    if mission_approval[0]:
      mission_commenced = True
    else:
      rejected_teams += 1
      turns += 1
      continue
  round_result = mission(mission_approval[1])
  turn += 1
  return round_result

def gameplay():
  global rounds_completed
  evil = 0
  good = 0
  while rounds_completed < 5:
    if evil == 3:
      return ("Evil wins!")
    if good == 3:
      guess = input("Guess the Merlin: ")
      if player_names.index(guess) == assigned_roles.index("Merlin"):
        return ("Evil wins!")
      else:
        return ("Good wins!")
    round_winner = round_player()
    if round_winner:
      good += 1
    else:
      evil += 1
    rounds_completed += 1
      
  
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
   

players = int(input("Enter number of players between 5 to 10: "))
assigned_roles = get_roles(players)
for player in range(players):
  player_name = input("Enter player name: ")
  player_names.append(player_name)

for player in range(players):
  print(f"{player_names[player]} is {assigned_roles[player]}")

print("\n"*25) # prevents players from seeing each other's roles
game_result = gameplay()