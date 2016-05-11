"""
'bootstrap.py' implements a bootstrap auditing procedure for a contest.
"""

from random import shuffle, choice
from utils  import agreement, roundup
from shared import SAMPLE_0, GROWTH_RATE, SAMPLE_DIVISOR

NPILES = 100  # Number of variant piles

# Returns the outcome of a t pile audit of a contest
#   @params
#     contest <Contest> : contest to audit
#   @return
#     <(str, int)> where the first element is the corrected outcome and the second
#     element is the number of ballots counted
def bootstrap_audit(contest):
  piles = [[] for n in range(NPILES)]
  start_idx = 0
  last_idx = SAMPLE_0
  shuffle(contest.ballots)
  while last_idx <= len(contest.ballots):
    s = contest.ballots[start_idx:last_idx]
    i = 0
    while i < last_idx - start_idx:
      for pile in piles:
        pile.append(choice(s))
      i += 1
    outcome = agreement(contest.candidates, piles + [contest.ballots[:last_idx]], \
                        contest.aggregator)
    if outcome:      
      return (outcome, last_idx)
    start_idx = last_idx
    last_idx = roundup(last_idx * GROWTH_RATE, SAMPLE_DIVISOR)
  return (contest.outcome[0], len(contest.ballots))
