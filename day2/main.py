from enum import Enum, auto

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def beats(self):
        match self:
            case Move.ROCK:
                return Move.SCISSORS
            case Move.PAPER:
                return Move.ROCK
            case Move.SCISSORS:
                return Move.PAPER

    def loses_by(self):
        match self:
            case Move.ROCK:
                return Move.PAPER
            case Move.PAPER:
                return Move.SCISSORS
            case Move.SCISSORS:
                return Move.ROCK

    def move_score(self):
        match self:
            case Move.ROCK:
                return 1
            case Move.PAPER:
                return 2
            case Move.SCISSORS:
                return 3
            case _:
                raise ValueError("error")

    @classmethod
    def to_move(cls, move):
        match move:
            case "A" | "X":
                return Move.ROCK
            case "B" | "Y":
                return Move.PAPER
            case "C" | "Z":
                return Move.SCISSORS
            case _:
                raise ValueError("error")

def calc_outcome_score(opp_move, my_move):
    match (opp_move, my_move):
        case (move1, move2) if move1 == move2:
            return 3
        case (move1, move2) if move2 == move1.beats():
            return 0
        case (move1, move2) if move2 == move1.loses_by():
            return 6
        case _:
            raise ValueError("error")

def part_one(filename):
    with open(filename) as f:
        moves = [tuple(line.split()) for line in f.readlines()]

    total_score = 0
    for move in moves:
        opp_move, my_move = Move.to_move(move[0]), Move.to_move(move[1])
        total_score += my_move.move_score()
        total_score += calc_outcome_score(opp_move, my_move)

    return total_score

def part_two(filename):
    with open(filename) as f:
        moves = [tuple(line.split()) for line in f.readlines()]
    total_score = 0
    for move, outcome in moves:
        opp_move = Move.to_move(move)
        match outcome:
            case "X":
                my_move = opp_move.beats()
            case "Y":
                my_move = opp_move
            case "Z":
                my_move = opp_move.loses_by()
        total_score += my_move.move_score()
        total_score += calc_outcome_score(opp_move, my_move)

    return total_score

input_path = "input.txt"
print(part_one(input_path))
print(part_two(input_path))