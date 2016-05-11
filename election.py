"""
'election.py' implements the Election class.
"""

class Election:
  # Election constructor
  #   @params
  #     contests <[Contest,]> : list of contests
  #   @return
  #     <Election>
  def __init__(self, contests):
    self.contests = contests

  # Computes contest outcomes
  #   @params
  #     None
  #   @return
  #     None
  def run(self):
    for contest in self.contests:
      contest.run()

  # Returns the result of a post-election, ballot-polling audit
  #   @params
  #     auditor <func> : function to run audit of election outcomes
  #   @return
  #     <[(str, int),]> where each entry is a tuple representing the reported winner
  #     and the number of ballots checked, respectively.
  def audit(self, auditor):
    return [auditor(contest) for contest in self.contests]
