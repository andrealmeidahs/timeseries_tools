from itertools import chain

def interval_overlap(*intervals):
    ij = sorted(intervals)
    return list(chain(*ij)) != sorted(chain(*ij))
