def allSame(ls: list) -> bool:
    if __isEmptyList(ls):
        return False
    if len(ls) == 1:
        return True
    fe = ls[0]
    for e in ls:
        if fe != e:
            return False
    return True


def __isEmptyList(ls: list) -> bool:
    return ls is None or len(ls) == 0
