def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    return len(arrivals) / 2 <= arrivals.index(name) < len(arrivals) - 1
