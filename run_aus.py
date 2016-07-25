"""
'run.py' runs an election with the specified options.
"""
import sys
from generators.rank_choice import rank_choice_from_aec_data,rank_choice_variant_sample

def main():
  ballots = rank_choice_from_aec_data({'counts' : 3})
  variant_ballots = rank_choice_variant_sample(ballots,{'nballots' : 20})
  print (rank_choice_from_aec_data)

if __name__ == '__main__':
  main()
