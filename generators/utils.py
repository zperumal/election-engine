"""
'utils.py' implements utility methods for the generating procedures.
"""

import numpy  as np
from numpy import asarray, add, vstack
from scipy.spatial.distance import euclidean as distance

# Returns euclidean distince between two points
#   @params
#     p1 <(int, int)> : point one
#     p2 <(int, int)> : point two
#   @return
#     <float> euclidean distance between two points
def euclid_dist(p1, p2):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(0.5)

# Returns numpy representation of votes
#   @params
#     ballot_list : list of votes
#   @return
#     numpy array representation of votes
def numpy_representation(ballot_list):
	return asarray(ballot_list)

# Returns list of tuple representation of votes
#   @params
#     ballot_array numpy array representation of votes
#   @return
#     ballot_list : list of votes
def tuple_representation(ballot_array):
	return tuple(map(tuple, ballot_array))

# Returns average vote for list
#   @params
#     ballot_array numpy array representation of votes
#   @return
#     average vote in array
def mean_votes(ballot_array):
	return ballot_array.mean(0)

# Returns median vote for list
#   @params
#     ballot_array numpy array representation of votes
#   @return
#     median vote in array
def median_votes(ballot_array):
	return np.median(ballot_array, axis=0)

# The improved adjustment towards the mean value
#	away from the target
#   @params
#     current_mean aveage ballot
#     new_ballot to potentially ad
#     target_mean average to move closer to
#   @return
#     distance between the initial_distance and the new_distance 
def improvement(ballots, new_ballot, target_mean, comparison__method=mean_votes):
	current_mean = mean_votes(ballots)
	initial_distance = distance(current_mean,target_mean)
	new_mean = mean_votes(vstack((ballots,new_ballot)))
	new_distance	 = distance(new_mean,target_mean)
	return initial_distance - new_distance
