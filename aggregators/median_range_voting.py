"""
'median_range_voting.py' implements a ballot aggregation procedure for median range
voting contests. 'median_range_voting_agg' determines the winner of a contest by the
candidate with the highest median score across all ballots. In ties, 
'median_range_voting_agg' will pick the first candidate with the highest median range
score in the 'result' tuple.
"""

from utils import median

# Returns winner and median range voting scores for contest
#   @params
#     candidates <(str,)>   : tuple of candidates
#     ballots    <[(int,),]> : ballots to aggregate
#   @return
#     <(str, (int,))> contest winner and median range voting score for each candidate
def median_range_voting_agg(candidates, ballots):
  result = tuple(median(_) for _ in zip(*ballots))
  return (candidates[result.index(max(result))], result)
