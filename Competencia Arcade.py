import random

games = ["Space Invaders", "Castlevania", "Street Fighters"]

people = []

for score in range(5):
    player = {
        "name": f"player {score+1}",
        "scores": {game: random.randint(50000, 1000000) for game in games}
    }
    people.append(player)
#print(people)

for player in people:
    player["Total Score"] = sum(player["scores"].values())
    #print(player)

winner = max(people, key=lambda player: player["Total Score"])

print("Arcade Game Scores:")
for player in people:
    print(f"{player['name']}: {player['scores']} (Total Score: {player['Total Score']})")

print("\nWinner:")
print(f"{winner['name']} wins with a total score of {winner['Total Score']}!")
