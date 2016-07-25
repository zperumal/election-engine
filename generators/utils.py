"""
'utils.py' implements utility methods for the generating procedures.
"""

import numpy  as np
from numpy import asarray, add, vstack
#from scipy.spatial.distance import euclidean as distance
from resources.dividebatur  import senatecount as sc 

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

# Parses input from AEC Western Australia 2013 election and returns matrix of ballot preferences for each count
# @params 
#	config_file path to config file 
#	out_dir 	path to out put directory
# @return
#	[[(str, ),],]  list of list of tuples corresponding t
def parse_aec_wa_2013_input(config_file='../resources/dividebatur/aec_fed2013_wa/aec_fed2013_wa.json',out_dir='./resources/dividebatur/angular/data/'):
  config_file = './resources/dividebatur/aec_fed2013_wa/aec_fed2013_wa.json'
  out_dir = './resources/dividebatur/angular/data/'
  sc_data = sc.get_data(config_file,out_dir)
  ballot_lists = []
  for row in sc_data:
    (candidates,atl,btl,tickets_for_count) = row
    atl_data = atl.raw_ticket_data
    btl_data = btl.raw_ticket_data
    total_data = atl.raw_ticket_data + btl.raw_ticket_data
    candidates = [x.CandidateID for x in candidates.candidates]
    filtered_data = [[candidate_id for (rank, candidate_id) in ballot]  for ballot in total_data if len(ballot) == len(candidates)]
    #TODO: (zperumal) handled partial ballots 
    ballot_lists.append(filtered_data)
  return ballot_lists