def hasSameContents(ls: list) -> bool:
    if ls is None:
        return False
    if len(ls) == 0:
        return False
    if len(ls) == 1:
        return True
    fe = ls[0]
    for e in ls:
        if fe != e:
            return False
    return True
