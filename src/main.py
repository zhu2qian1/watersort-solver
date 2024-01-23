from listHelper import hasSameContents


class Move:
    def __init__(self, fromIdx: int, toIdx: int, clr: int) -> None:
        self.fromIdx = fromIdx
        self.toIdx = toIdx
        self.clr = clr


class WaterSortPuzzle:
    def __init__(self, tubes: list[list[int]]) -> None:
        self.tubes = tubes
        self.moves: list[Move] = list()

    @staticmethod
    def factory(stdin: list[str]):
        return WaterSortPuzzle([list(map(int, e.split(" "))) for e in stdin])

    def isSolved(self) -> bool:
        if not hasSameContents(self.tubes):
            return False
        return True

    def __repr__(self) -> str:
        return f"WaterSortPuzzle: tubes: {self.tubes}"

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

    # TODO 1個ずつ移動のパターンしかチェックしてないので2個とか3個とかのケースを調べる
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
        if self.tubes[to_] == [0, 0, 0, 0]:  # 全部カラのケース
            return True
        if self.tubes[to_][4 - size - 1] != color:
            return False
        return True


def main() -> int:
    game = WaterSortPuzzle.factory(readStdin())
    print(game.__repr__())
    print(game.isSolved())
    return 0


def readStdin() -> list[str]:
    ret: list[str] = list()
    while True:
        s = input()
        if not s:
            break
        ret.append(s)
    return ret


if __name__ == "__main__":
    main()
