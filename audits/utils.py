"""
'utils.py' implements utility methods for the auditing procedures.
"""

from math import ceil

# Returns x rounded to next multiple of k
#   @params
#     x <int> : number to round up
#     k <int> : multiple to round up to
#   @return
#     <int> x rounded up to next multiple of k
def roundup(x, k):
  return int(ceil(x / float(k))) * k

# Returns outcome agreement or False if no agreement
#   @params
#     candidates <(str,)>      : list of candidates
#     piles      <[[(int,),],] : list of lists of ballots
#     aggregator <func>        : aggregator function
#   @return
#     <str|boolean> winner agreed upon or False if no agreement
def agreement(candidates, piles, aggregator):
   outcomes = [aggregator(candidates, pile)[0] for pile in piles]
   return outcomes[0] if all(o == outcomes[0] for o in outcomes) else False

# Returns number of votes in each candidates favor
#   @params
#     candidates <(str,)>    : tuple of candidates
#     ballots    <[(int,),]> : list of ballots
#   @return
#     <[int,]> list of number of votes in each candidates favor
def merge_counts(candidates, ballots):
  result = [0 for _ in candidates]
  for ballot in ballots:
    result[ballot.index(max(ballot))] += 1
  return result
