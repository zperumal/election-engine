"""
'rank_choice.py' implements a ballot generation procedure for rank choice
contests. 
"""
from random import shuffle
from resources.sp2 import test_sample, sample
from generators.utils import parse_aec_wa_2013_input

# Returns a list of ballots from a input data file
#   @params
#	 params		<{str:int|float}	
#   @return
#   <[(int,),]> ballots  
def rank_choice_from_aec_data(params):
	#TODO: (zperumal) enable multiple counts
	count_index = params['counts'] 
	ballots = parse_aec_wa_2013_input()[count_index]
	return ballots

# Returns a set of variant ballots based on sp2
#   @params
#	 params		<{str:int|float}	
#   @return
#   <[(int,),]> ballots  
def rank_choice_variant_sample(ballots,params):
	nballots = params['nballots']
	return sample(ballots,nballots,printing_wanted=False)



# Returns a list of ballots 
#   @params
#    candidates <(str,)>: tuple of candidates
#	 params		<{str:int|float}	
#   @return
#   <[(int,),]> ballots  

def rank_choice_test_data(candidates,params):
	ballots = []					#Set of ballots generated
	ncandidates = len(candidates)	# Number of candidates in contest
	nballots = params['nballots']	# Number of ballots to generate

	#Generate ballots with random ranking of candidates 
	for _ in range(nballots):
		ranking = list(range(ncandidates))
		shuffle(ranking)
		ballots.append(ranking)
	return ballots

ballots = rank_choice_test_data(('A','B','C'),{'nballots' : 10})



