import json

def open_file(filename: str="best_score.json") -> int:

    with open(filename, "r") as data:
        best_score = json.load(data)

    return best_score["Record"]


def write_record_tofile(best_score: int, filename: str="best_score.json") -> None:

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({"Record": best_score}, file)