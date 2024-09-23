from getpass import getpass as input

# 2 player rock,  paper, scissors.

# define 2 players
print("Lets play a game!")
print("""r = rock
p = paper
s = scissers.""")
player_one = input("Player one: r, p, s")
player_two = input("Player two: r, p, s")
# define rock, paper, scissors.
# scissors > paper
# paper > rock
# rock > scissors
#if (player_one == "r" or player_two == "r"):
# print("Draw")
if (player_one == "p" and player_two == "p") or (
    player_one == "r" and player_two == "r") or (player_one == "s"
                                                 and player_two == "s"):
  print("Draw")
elif (player_one == "s" and player_two == "p"):
  print("Player one wins with scissers")
elif (player_one == "p" and player_two == "r") or (
    player_one == "s" and player_two == "p") or (player_one == "r"
                                                 and player_two == "s"):
  print("Player one wins!")
elif (player_two == "p" and player_one == "r") or (
    player_two == "s" and player_one == "p") or (player_two == "r"
                                                 and player_one == "s"):
  print("Player two wins!")
else:
  print("try again")
