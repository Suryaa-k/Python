from functools import lru_cache

@lru_cache(maxsize=None)
def unique(r: int, c: int) -> int:
    if r == 0 and c == 0:
        return 1
    if r < 0 or c < 0:
        return 0
    return unique(r, c - 1) + unique(r - 1, c)

def noof(n: int, m: int) -> int:
    return unique(n - 1, m - 1)