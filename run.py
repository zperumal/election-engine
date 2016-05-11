"""
'run.py' runs an election with the specified options.
"""

from sys         import argv
from time        import time
from contest     import Contest
from election    import Election
from utils       import summarize
from config      import AUDITS, CONTESTS

NTRIALS = 1 if len(argv) < 2 else int(argv[1])

results = {}
for cname in CONTESTS:
  results[cname] = {aname : {'e':0, 'n':0} for aname in AUDITS}

def main():
  # Run Experiments
  start = time()
  for cname in sorted(CONTESTS):
    for t in xrange(NTRIALS):
      cattr = CONTESTS[cname]
      c, g, a, params = cattr['c'], cattr['g'], cattr['a'], cattr['p']
      contest = Contest(c, g, a, params)
      e = Election([contest])
      e.run()
      for aname in sorted(AUDITS):
        outcome, nballots = e.audit(AUDITS[aname])[0]  # assumes 1 contest
        if outcome != contest.outcome[0]:
          results[cname][aname]['e'] += 1
        results[cname][aname]['n'] += nballots
  end = time()

  # Report Results
  for cname in sorted(CONTESTS):
    print cname
    for aname in sorted(AUDITS):
      avg_nballots = results[cname][aname]['n'] / float(NTRIALS)
      avg_nerrors = results[cname][aname]['e'] / float(NTRIALS)
      print '\t%s\t%f\t%f' % (aname, avg_nballots, avg_nerrors)
  print 'Runtime: ' + str(end - start)

if __name__ == '__main__':
  main()
