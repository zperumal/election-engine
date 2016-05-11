"""
'utils.py' implements utility methods for the eleciton engine.
"""

# Returns summary of election audit
#   @params
#     audits <[(True|str, int)]> : list of audit results where first item is True
#                                  if audit matched reported outcome or corrected
#                                  outcome and the second item is the number of 
#                                  ballots checked
#   @return
#     <str> summary of election audit
def summarize(audits):
  s = 'Election Audit Summary\n'
  for i in xrange(len(audits)):
    s += '\tContest ' + str(i) + '\n'
    outcome, nballots = audits[i]
    if outcome == True:
      s += '\t\tCONFIRMED after ' + str(nballots) + '\n'
    else:
      s += '\t\tWRONG     after ' + str(nballots) + '\n'
  return s
