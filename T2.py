n = int(input("Введіть кількість друзів: "))

all_games = set()

for i in range(n + 1):
    if i == 0:
        games = input("Введіть свої ігри через кому: ")
        all_games = set(games.split(","))
    else:
        games = input("Введіть ігри друга через кому: ")
        friend_games = set(games.split(","))
        all_games = all_games & friend_games

print("Ігри, в які можуть грати всі:", all_games)