from itertools import chain

def interval_overlaps(*intervals):
    """
        Tests whether any of the interval in argument overlaps
        Accepts any number of intervals defined as strat and endpoint

        > interval_overlaps([1,2],[3,4])

        rerturns False
    """
    ij = sorted(intervals)
    return list(chain(*ij)) != sorted(chain(*ij))

def interval_intersection(*intervals):
    """
        Returns the interval corresponding to the
        intersection of two intervals
        
        > interval_intersection([1,3],[2,4])

        rerturns [2,3]
    """
    max_st = max(ij[0] for ij in intervals)
    min_end = min(ij[1] for ij in intervals)
    if max_st < min_end:
        return (max_st, min_end)

def interval_list_overlaps(il1, il2):
    """
        Given two lists of intervals, returns the indices
        of the intervals that overlap

        > interval_list_overlaps([(1,3),(4,6)],[(2,3.5),(7,8)])

        returns [(1,1)]
    """
    index_list = []
    for n1, i1 in enumerate(il1):
        for n2, i2 in enumerate(il2):
            if interval_overlaps(i1, i2):
                index_list.append((n1,n2))

    return index_list
                
    
