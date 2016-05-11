"""
'mean_range_voting.py' implements a ballot aggregation procedure for mean range voting
contests. 'mean_range_voting_agg' determines the winner of a contest by the candidate
with the highest mean score across all ballots. In ties, 'mean_range_voting_agg' will
pick the first candidate with the highest mean range score in the 'result' tuple.
"""

# Returns winner and mean range voting scores for contest
#   @params
#     candidates <(str,)>   : tuple of candidates
#     ballots    <[(int,),]> : ballots to aggregate
#   @return
#     <(str, (float,))> contest winner and mean range voting score for each candidate
def mean_range_voting_agg(candidates, ballots):
  result = tuple(sum(_)  / float(len(ballots)) for _ in zip(*ballots))
  return (candidates[result.index(max(result))], result)
