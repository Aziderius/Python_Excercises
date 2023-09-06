import random
from typing import List

games = ["Space Invaders", "Castlevania", "Street Fighters"]

class Player:
    def __init__(self, name: str, scores, total_score = 0) -> None:
        self.name = name
        self.scores = scores
        self.total_score = total_score

people: List[Player] = []

for score in range(5):
    player = Player(
        name=f"player {score+1}",
        scores={game: random.randint(50000, 1000000) for game in games}
    )
    player.total_score = sum(player.scores.values())
    people.append(player)

winner = max(people, key=lambda player: player.total_score)

print("Arcade Game Scores:")
for player in people:
    print(f"{player.name}: {player.scores} (Total Score: {player.total_score})")

print("\nWinner:")
print(f"{winner.name} wins with a total score of {winner.total_score}!")
