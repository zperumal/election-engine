"""
'simple_plurality.py' implements a ballot aggregation procedure for simple plurality 
contests. In ties, 'simple_plurality_agg' will pick the first candidate with the most
votes in the aggregated 'result' tuple.
"""

# Returns winner and aggregated vote counts for simple plurality contest
#   @params
#     candidates <(str,)>   : tuple of candidates
#     ballots    <[(int,),]> : ballots to aggregate
#   @return
#     <(str, (int,))> contest winner and aggregated vote counts for each candidate
def simple_plurality_agg(candidates, ballots):
  result = tuple(sum(_) for _ in zip(*ballots))
  return (candidates[result.index(max(result))], result)
