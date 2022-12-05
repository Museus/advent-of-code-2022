import pathlib
from typing import Mapping

PLAYBOOK_FILE = "day_2.txt"
PLAYER_1_NAME = "Player 1"
PLAYER_2_NAME = "Player 2"

class Shape:
    points: int
    player_1_code: str
    player_2_code: str

    def get_points_against(self, other: "Shape"):
        if self < other:
            match_points = 0
        elif self == other:
            match_points = 3
        elif self > other:
            match_points = 6

        return self.points + match_points

class Rock(Shape):
    points = 1
    name = "Rock"

    def __lt__(self, other: "Shape"):
        return isinstance(other, Paper)

    def __eq__(self, other: "Shape"):
        return isinstance(other, Rock)

class Paper(Shape):
    points = 2
    name = "Paper"

    def __lt__(self, other: "Shape"):
        return isinstance(other, Scissors)

    def __eq__(self, other: "Shape"):
        return isinstance(other, Paper)

class Scissors(Shape):
    points = 3
    name = "Scissors"

    def __lt__(self, other: "Shape"):
        return isinstance(other, Rock)

    def __eq__(self, other: "Shape"):
        return isinstance(other, Scissors)

def get_shape(code: str):
    if code.upper() in ("A", "X"):
        return Rock()

    if code.upper() in ("B", "Y"):
        return Paper()

    if code.upper() in ("C", "Z"):
        return Scissors()

def load_playbook_file(playbook_file_path: pathlib.Path):
    with open(playbook_file_path, "r") as input_file:
        return input_file.readlines()

def simulate_round(line: str):
    player_1, player_2 = map(get_shape, line.strip().split(" "))

    print(f"{PLAYER_1_NAME} plays {player_1.name} against {PLAYER_2_NAME}'s {player_2.name}.")
    print(f"{PLAYER_1_NAME} gets {player_1.get_points_against(player_2)} points.")
    print(f"{PLAYER_2_NAME} gets {player_2.get_points_against(player_1)} points.")

    return (player_1.get_points_against(player_2), player_2.get_points_against(player_1))

def print_leaderboards(leaderboards: Mapping[str, int]):
    if not leaderboards[PLAYER_1_NAME] == leaderboards[PLAYER_2_NAME]:
        sorted_leaderboards = sorted(leaderboards.items(), key=lambda x: x[1], reverse=True)
        print(f"{sorted_leaderboards[0][0]} wins with {sorted_leaderboards[0][1]} points!")
        print(f"{sorted_leaderboards[1][0]} follows up with {sorted_leaderboards[1][1]} points.")
    else:
        print(f"It's a tie! Both players have {leaderboards[PLAYER_1_NAME]} points.")

playbook_file_path = pathlib.Path(PLAYBOOK_FILE)

print("Running simulation...")
leaderboards = {
    PLAYER_1_NAME: 0,
    PLAYER_2_NAME: 0,
}

for idx, line in enumerate(load_playbook_file(playbook_file_path)):
    round_title = f"Round {idx+1}"

    print(f"\n{round_title}\n{'-' * len(round_title)}")

    round_points = simulate_round(line)
    leaderboards[PLAYER_1_NAME] += round_points[0]
    leaderboards[PLAYER_2_NAME] += round_points[1]

print(f"\nAfter {idx+1} rounds:")
print_leaderboards(leaderboards)