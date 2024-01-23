def hasSameContents(ls: list) -> bool:
    if __isFalsyList(ls):
        return False
    if len(ls) == 1:
        return True
    fe = ls[0]
    for e in ls:
        if fe != e:
            return False
    return True


def hasTruthyContent(ls: list) -> bool:
    if __isFalsyList(ls):
        return False
    for e in ls:
        if e:
            return True
    return False



def __isFalsyList(ls: list) -> bool:
    if ls is None:
        raise Exception("list is None")
    return len(ls) != 0
