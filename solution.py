

def solve(value):
    return {r["id"]: r for r in value} if len({r["id"] for r in value}) == len(value) else (_ for _ in ()).throw(ValueError("duplicate id"))
