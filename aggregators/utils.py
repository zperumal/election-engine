"""
'utils.py' implements utility methods for the aggregating procedures.
"""

from numpy import median as np_median, array

# Returns median of list
#   @params
#     l <[int,]> : list
#   @return
#     <int> median
def median(l):
    return np_median(array(l))
