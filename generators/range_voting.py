"""
'range_voting.py' implements a ballot generation procedure for range voting contests.
'range_voting_gen' generates candidate profiles using Yee Pictures 
(http://rangevoting.org/IEVS/Pictures.html) where each candidate is a point on a 2-D
space of size 'YEE_PICTURE_SIDE' by 'YEE_PICTURE_SIZE'.

    ''''''''''''''''''''''
    '                    '  Voters are then chosen from this space at random and the
    '                  C '  range voting score assigned to each candidate for that 
    '   A                '  voter is equal to the euclidean distance between that
    '                    '  voter's profile (point on Yee Picture) and the candidate's
    '                    '  profile divided by the 'MAX_DIST', or the maximum distance
    '       B            '  possible between two profiles in the Yee Picture (equal to
    '                    '  the diagonal of the Yee Picture), times the 'max_range', or
    '                    '  maximum score for contest range.
    ''''''''''''''''''''''

'range_voting_gen' assumes the minimum of the contest score range to be 0.
"""

from random import randint
from utils  import euclid_dist

YEE_PICTURE_SIDE = 1000

# Maximum distinace possible in Yee Picture (corresponds to diagonal of plane)
MAX_DIST = int(euclid_dist((0,0), (YEE_PICTURE_SIDE, YEE_PICTURE_SIDE)))

# Returns a range voting contest
#   @params
#     candidates <(str,)> : tuple of candidates
#   @return
#     <[(int,),]> ballots
def range_voting_gen(candidates, params):
  ballots = []                    # Set of ballots generated
  ncandidates = len(candidates)   # Number of candidates in contest
  nballots = params['nballots']   # Number of ballots to generate
  range_max = params['range_max'] # Maximum score for range vote ballot

  # Generate random candidate profiles within Yee Picture
  candidate_profiles = [(randint(0, MAX_DIST), randint(0, MAX_DIST)) \
                        for _ in xrange(ncandidates)]

  for _ in xrange(nballots):
    voter_profile = (randint(0, MAX_DIST), randint(0, MAX_DIST))
    ballot = tuple(int(range_max * (euclid_dist(voter_profile, candidate_profiles[i]) \
      / float(MAX_DIST))) for i in xrange(ncandidates))
    ballots.append(ballot)

  return ballots
