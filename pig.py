import random
print("Welcome to Pig!")
print("You roll and get points,first to get at least 50 pts wins")
print("By rolling you get a current score that at the end of the turn is added to your total player score")
print("If you roll 1,your current score turns 0")
def roll():
    min_value = 1
    max_value = 6
    random_number = random.randint(min_value, max_value)
    return random_number

while True:
  nr_of_players = input("How many players?(maxim 4) ")
  if nr_of_players.isdigit():
      nr_of_players = int(nr_of_players)
      if 1< nr_of_players <5:
         break
      else:
         print("Too many,at most 4 ")
  else:
      print("Choose a number between 1 and 4: ")


names = [0 for i in range(nr_of_players)]
for i in range(nr_of_players):
    names[i] = input("Enter your name: ")

max_score = 50
score = [0 for i in range(nr_of_players)]
print(score)
while max(score) < max_score:
   for player in range(nr_of_players):
       current_score = 0
       print(f"Current player:{names[player]}")
       print(f"Current score:{score[player]}")
       while True:
         turn = input("Do you want to roll?(y): ")
         if turn.lower() != "y":
           break

         value = roll()
         if value == 1:
               current_score = 0
               print("You rolled 1,your score is: 0")
               print("Next player")
               break
         else:
               current_score += value
               print(f"You rolled {value} ")

         print(f"Current score: {current_score}")
       score[player] += current_score
       print(f"{names[player]}'s score is:", score[player])
       if score[player] >= max_score:
           break
   if max(score) >= max_score:
       break

winner = names[score.index(max(score))]
print(f"The winner is {winner}")