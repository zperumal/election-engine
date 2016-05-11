"""
'diffsumscore.py' implements the DiffSumScore auditing procedure for a contest.
"""

from random import shuffle
from utils  import roundup
from shared import SAMPLE_0, GROWTH_RATE, SAMPLE_DIVISOR

C = 5  # Controls error rate

# Returns whether agreement over DiffSum rule for any candidate
#   @params
#     contest <Contest> : contest to audit  
#     sample  <[(str,)] : list of ballots
#   @return
#     <str|boolean> winner agreed upon or False if no agreement
def diffsumscore(contest, sample):
  ncandidates = len(contest.candidates)
  result = contest.aggregator(contest.candidates, sample)[1]
  b, a = sorted(list(result))[-2:]
  if (a - b)**2 > C * (a + b):
    return contest.candidates[result.index(a)]
  return False

# Returns the outcome of a DiffSumScore audit of a contest
#   @params
#     contest <Contest> : contest to audit
#   @return
#     <(str, int)> where the first element is the corrected outcome and the second
#     element is the number of ballots counted
def diffsumscore_audit(contest):
  s_size = SAMPLE_0
  shuffle(contest.ballots)
  nballots = len(contest.ballots)
  while s_size < nballots:
    sample = contest.ballots[:s_size]
    outcome = diffsumscore(contest, sample)
    if outcome:
      return (outcome, s_size)
    s_size = roundup(s_size * GROWTH_RATE, SAMPLE_DIVISOR)
  return (contest.outcome[0], nballots)
