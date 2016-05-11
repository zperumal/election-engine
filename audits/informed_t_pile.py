"""
'informed_t_pile.py' implements a t-pile auditing procedure for a contest, augmented with
semi random vote distribution to improve convergence 
"""

from itertools              import chain
from random                 import shuffle
from utils                  import agreement, roundup
from numpy                  import asarray, add, vstack
from scipy.spatial.distance import euclidean as distance
from shared                 import SAMPLE_0, GROWTH_RATE, SAMPLE_DIVISOR

NPILES = 7  # Number of piles

# Returns the outcome of an informed t-pile audit of a contest
#   @params
#     contest <Contest> : contest to audit
#   @return
#     <(str, int)> where the first element is the corrected outcome and the second
#     element is the number of ballots counted
def informed_t_pile_audit(contest):
  piles =[[]  for n in range(NPILES)]

  start_idx = 0
  last_idx = SAMPLE_0
  shuffle(contest.ballots)

  # Initial Random Ballots
  for i in xrange(start_idx, last_idx):
      piles[i % NPILES].append(contest.ballots[i])

  start_idx = last_idx
  last_idx = roundup(last_idx * GROWTH_RATE, SAMPLE_DIVISOR)

  while last_idx <= len(contest.ballots):
    combined_piles = list(chain(*piles))
    total_score = contest.aggregator(contest.candidates, combined_piles)[1]
    
    remaining_piles = set(range(NPILES))
    round_pile_size = last_idx / SAMPLE_DIVISOR

    for i in xrange(start_idx, last_idx):
      ballot = contest.ballots[i]
      max_index, max_value = None , None

      random_remaining_piles = list(remaining_piles)
      shuffle(random_remaining_piles)
      for pile_index in random_remaining_piles:
        current_score = contest.aggregator(contest.candidates, piles[pile_index])[1]
        score_with_new_ballot = contest.aggregator(contest.candidates, piles[pile_index] + [ballot])[1]
        improvement = distance(current_score,total_score) - distance(score_with_new_ballot,total_score)
        if max_value == None or improvement > max_value:
          max_value, max_index = improvement, pile_index
      if max_index == None:
        raise Exception("ERROR: Max index is None")
      piles[max_index].append(ballot)
      if len(piles[max_index]) == round_pile_size:
        remaining_piles.remove(max_index)
    length = [len(pile) for pile in piles]
    if length.count(length[0]) != len(length):
      raise Exception("Piles non uniform size")
    outcome = agreement(contest.candidates, piles, contest.aggregator)
    if outcome:
      return (outcome, last_idx)
    start_idx = last_idx
    last_idx = roundup(last_idx * GROWTH_RATE, SAMPLE_DIVISOR)
  return (contest.outcome[0], last_idx)
