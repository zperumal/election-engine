"""
'simple_plurality.py' implements a ballot generation procedure for simple plurality
contests. 'simple_plurality_gen' generates two kinds of contests:

  (1) Two candidate contest where A has 'ratio' * 'nballots' votes compared to B.
  (2) Four candidate contest where candidate 'i' has 'FOUR_CANDIDATE_BALLOT_RATIO[i]'
      * 'nballots' votes.

'simple_plurality_gen' generates 0 ballots when len(candidates) != 2, 4.
"""

FOUR_CANDIDATE_BALLOT_RATIOS = [0.4, 0.3, 0.2, 0.1]

# Returns a simple plurality contest
#   @params
#     candidates <(str,)>          : tuple of candidates
#     params     <{str:int|float} : parameters to specify contest generation
#   @return
#     <[(int,),]> ballots
def simple_plurality_gen(candidates, params):
  ballots = []                   # Set of ballots generated
  ncandidates = len(candidates)  # Number of candidates in contest
  nballots = params['nballots']  # Number of ballots to generate
  ratio = params['ratio']        # Ratio of votes for A over B in two candidate contest

  # Two candidate contest
  if ncandidates == 2:
    for i in xrange(ncandidates):
      ballot = tuple(i == j for j in xrange(ncandidates))
      nballots_for_candidate = int((ratio if i == 0 else 1 - ratio) * nballots)
      ballots += [ballot for _ in xrange(nballots_for_candidate)]

  # Four candidate contest
  elif ncandidates == 4:
    for i in xrange(ncandidates):
      ballot = tuple(i == j for j in xrange(ncandidates))
      nballots_for_candidate = int(FOUR_CANDIDATE_BALLOT_RATIOS[i] * nballots)
      ballots += [ballot for _ in xrange(nballots_for_candidate)]

  return ballots
