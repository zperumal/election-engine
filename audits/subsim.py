"""
'subsim.py' implements the SubSim auditing procedure for a contest.
"""

from utils  import roundup
from random import shuffle, sample as pop_sample
from shared import SAMPLE_0, GROWTH_RATE, SAMPLE_DIVISOR

SUBSET_RATIO = 0.7  # Ratio of sample used to generate margin matrix
NSIM_TRIALS = 1000  # Number of margin matrices simulated
ALPHA = 0.05        # Percent of samples that do not agree after subsampling

# Returns winner of subsampling simulations and ratio of wins for all simulations
#   @params
#     contest <Contest>   : contest to audit
#     sample  <[(int,),]> : sample of ballots
#   @return
#     <(str, float)> winning candidate of simulations and ratio of wins
def subsample(contest, sample):
  ncandidates = len(contest.candidates)
  wins = [0 for _ in xrange(ncandidates)]
  for i in xrange(NSIM_TRIALS):
    variant_sample = pop_sample(sample, int(len(sample) * SUBSET_RATIO))
    winner = contest.aggregator(contest.candidates, variant_sample)[0]
    wins[contest.candidates.index(winner)] += 1
  winner_idx = wins.index(max(wins))
  return (contest.candidates[winner_idx], wins[winner_idx] / float(NSIM_TRIALS))

# Returns the outcome of a subsampling simulation audit of a contest
#   @params
#     contest <Contest> : contest to audit
#   @return
#     <(str, int)> where the first element is the corrected outcome and the second
#     element is the number of ballots counted
def subsim_audit(contest):
  s_size = SAMPLE_0
  shuffle(contest.ballots)
  nballots = len(contest.ballots)
  while s_size < nballots:
    sample = contest.ballots[:s_size]
    winner, win_ratio = subsample(contest, sample)
    if win_ratio >= 1 - ALPHA:
      return (winner, s_size)
    s_size = roundup(s_size * GROWTH_RATE, SAMPLE_DIVISOR) 
  return (contest.outcome[0], nballots)
