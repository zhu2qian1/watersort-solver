from listHelper import allSame
import json
import sys
from functools import reduce
from operator import and_


class Move:
    def __init__(self, fromIdx: int, toIdx: int) -> None:
        self.fromIdx = fromIdx
        self.toIdx = toIdx


class WaterSortPuzzle:
    def __init__(self, tubes: list[list[int]]) -> None:
        self.tubes = tubes
        self.moves: list[Move] = list()

    @staticmethod
    def factory(puzzle: list[str]):
        return WaterSortPuzzle([list(map(int, e.split(" "))) for e in puzzle])

    def isSolved(self) -> bool:
        return reduce(and_, [allSame(tube) for tube in self.tubes])

    def __repr__(self) -> str:
        return f"WaterSortPuzzle: tubes: {self.tubes}"

    # TODO Moveって可逆的か調べる
    def makeMove(self, move: Move) -> None:
        pass

    def solve(self) -> bool:
        if self.isSolved():
            return True
        for f in range(len(self.tubes)):
            for t in range(len(self.tubes)):
                if f == t:
                    continue
        return False

    def isMovable(self, from_: int, to_: int) -> bool:
        # 移動元のチェック
        if self.tubes[from_] == [0, 0, 0, 0]:  # 全部カラのケース
            return False
        color, size = None, 0
        for ptr in range(3, -1, -1):  # 3, 2, 1, 0
            ptrclr = self.tubes[from_][ptr]
            if ptrclr == 0:  # 0 だった場合は飛ばして下の段を検査
                continue
            if size == 0:
                color = ptrclr
                size = 1
                continue
            if size >= 1 and ptrclr == color:
                size += 1
                continue
            break

        if color is None or size <= 0:
            raise Exception(f"実装に不備あり。 color={color}, size={size}")

        # 移動先のチェック
        if self.tubes[to_][4 - size]:  # 移動先にすでに水がある場合は無理
            return False
        if not any(self.tubes[to_]):  # 全部カラ
            return True
        if size == 4:  # 全部カラではない かつ 移動元が4段なら確実に移動不可
            return False
        if self.tubes[to_][4 - size - 1] != color:
            return False
        return True


def main(*args) -> int:
    game = WaterSortPuzzle(
        read_game_json(args[1] if len(args) > 1 else "./resources/json/example.json")
    )
    print(game.__repr__())
    print(game.isSolved())
    return 0


def read_game_json(path: str = None) -> list[list[int]]:
    game_json = None
    with open(path, "r", encoding="utf-8") as f:
        game_json = json.load(f)
    # check file content
    if not isinstance(game_json, list):
        raise TypeError(
            f"invalid type of json. (expteced list, but got {type(game_json)})"
        )
    if not len(game_json) >= 4:
        raise TypeError(
            f"json list size is too small. (expected len >= 4, but got {len(game_json)})"
        )
    for tube in game_json:
        if not isinstance(tube, list):
            raise TypeError(
                f"invalid type of element. (expected list, but got {type(tube)})"
            )
        if len(tube) != 4:
            raise ValueError(f"invalid tube length. (expected 4, but got {len(tube)})")
        for e in tube:
            if not isinstance(e, int):
                raise TypeError(
                    f"invalid type of element. (expected int, but got {type(e)})"
                )
            if not e >= 0:
                raise ValueError(
                    f"non-positive number contained. (expected value >= 0, but got {e})"
                )
    return game_json


if __name__ == "__main__":
    main(*sys.argv)
