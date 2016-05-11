"""
'bayes.py' implements a bayesian auditing procedure for a contest.
"""

from utils  import merge_counts, roundup
from random import gammavariate, shuffle
from shared import SAMPLE_0, GROWTH_RATE, SAMPLE_DIVISOR

NSIM_TRIALS = 20000  # Number of simulations to run for Gamma Variates
ALPHA = 0.05         # Risk limiting threshold

# Returns index of candidate that won simulated tally
#   @params
#     candidates  <(str,)> : tuple of candidates
#     vote_counts <(int,)> : number of voters who favored each candidate
#     nballots    <int>    : number of ballots in contest
#   @return
#     <int> index of candidate that won tally
def tally(candidates, vote_counts, nballots):
  ncandidates = len(candidates)
  gvariates = [gammavariate(1 + vote_counts[i], 1) for i in xrange(ncandidates)]
  gvsum = float(sum(gvariates))
  result = tuple(vote_counts[i] + (nballots - sum(vote_counts)) \
    * gvariates[i] / gvsum for i in xrange(ncandidates))
  return result.index(max(result))

# Returns the winner and winner's probability over simulated tally trials
#   @params
#     candidates <(str,)>    : tuple of candidates
#     sample     <[(int,),]> : sample of ballots
#     nballots   <int>       : number of ballots in contest
#   @return
#     <(str, float)> winner and probability that winner won
def compute_win_probs(candidates, sample, nballots):
  wins = [0 for _ in candidates]
  vote_counts = merge_counts(candidates, sample)
  for i in xrange(NSIM_TRIALS):
    winner_idx = tally(candidates, vote_counts, nballots)
    wins[winner_idx] += 1
  winner_idx = wins.index(max(wins))
  return (candidates[winner_idx], wins[winner_idx] / float(NSIM_TRIALS))

# Returns the outcome of a bayesian audit of a contest
#   @params
#     contest <Contest> : contest to audit
#   @return
#     <(str, int)> where the first element is the corrected outcome and the second
#     element is the number of ballots counted
def bayes_audit(contest):
  s_size = SAMPLE_0
  shuffle(contest.ballots)
  nballots = len(contest.ballots)
  while s_size < nballots:
    sample = contest.ballots[:s_size]
    winner, win_prob = compute_win_probs(contest.candidates, sample, nballots)
    if win_prob >= (1 - ALPHA):
      return (winner, s_size)
    s_size = roundup(s_size * GROWTH_RATE, SAMPLE_DIVISOR)
  return (contest.outcome[0], nballots)
