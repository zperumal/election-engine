"""
'contest.py' implements the Contest class.
"""

class Contest:
  # Contest constructor
  #   @params
  #     candidates <(str,)>         : tuple of candidates
  #     generator  <func>           : function to generate contest ballots
  #     aggregator <func>           : function to compute outcome of contest
  #     params     <{str:int|float} : parameters to specify contest generation
  #   @return
  #     <Contest>
  def __init__(self, candidates, generator, aggregator, params):
    self.candidates = candidates
    self.aggregator = aggregator
    self.ballots = generator(candidates, params)

  # Computes contest outcome
  #   @params
  #     None
  #   @return
  #     None
  def run(self):
    self.outcome = self.aggregator(self.candidates, self.ballots)
