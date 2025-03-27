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

def interval_list_overlaps_brute(il1, il2, ignore_missing=False):
    """
        Given two lists of intervals, returns the indices
        of the intervals that overlap

        > interval_list_overlaps([(1,3),(4,6)],[(2,3.5),(7,8)])

        returns [(1,1)]

        Note: this brute-force approach is realy slow and could be
        improved, for instance by filtering out first intervals
        that cannot overlap
    """
    index_list = []
    for n1, i1 in enumerate(il1):
        for n2, i2 in enumerate(il2):
            try:
                if interval_overlaps(i1, i2):
                    index_list.append((n1,n2))
            except Exception as e:
                if ignore_missing:
                    continue
                else:
                    raise e

    return index_list
                
    
def interval_list_overlaps(il1, il2, ignore_missing=False):
    """
        Given two lists of intervals, returns the indices
        of the intervals that overlap

        > interval_list_overlaps([(1,3),(4,6)],[(2,3.5),(7,8)])

        returns [(1,1)]

    """
    index_list = []
    il2filt = [(n2,i2) for n2,i2 in enumerate(il2) if i2 is not None]
    sil2start = sorted( il2filt, key=lambda intvl: intvl[1][0])
    #sil2end = sorted( il2filt, key=lambda intvl: intvl[1])
    for n1, i1 in enumerate(il1):
        # first interval in i2 that starts after the end of current i1
        imax = [i2[0] > i1[1] for n2,i2 in sil2start].index(True)
        possible_i2 = sil2start[:imax]
        # i2 intervals that end after i1 starts
        possible_idx = [ii for ii, intv in (possible_i2) if intv[1]<i1[0]]
        for n2 in possible_idx:
            index_list.append((n1,n2))

    return index_list
