"""
'config.py' implements large global data structures.
"""

from audits.bayes           import bayes_audit
from audits.t_pile          import t_pile_audit
from audits.bootstrap       import bootstrap_audit
from audits.subsim          import subsim_audit
from audits.diffsumscore    import diffsumscore_audit
from audits.informed_t_pile import informed_t_pile_audit

from generators.range_voting     import range_voting_gen
from generators.simple_plurality import simple_plurality_gen

from aggregators.simple_plurality    import simple_plurality_agg
from aggregators.mean_range_voting   import mean_range_voting_agg
from aggregators.median_range_voting import median_range_voting_agg

NBALLOTS = 100000  # Number of ballots per contest
RANGE_MAX = 100    # Range voting max score

AUDITS = {
  '1: T Pile'          : t_pile_audit,
  '2: Bootstrap'       : bootstrap_audit,
  '3: Bayesian'        : bayes_audit,
  '4: DiffSumScore'    : diffsumscore_audit,
  '5: SubSim'          : subsim_audit,
  '6: Informed T Pile' : informed_t_pile_audit
}

CONTESTS = {
  '01: 2-Candidate Simple Plurality - 0.7500' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.7500
    }
  },
  '02: 2-Candidate Simple Plurality - 0.7000' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.7000
    }
  },
  '03: 2-Candidate Simple Plurality - 0.6500' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.6500
    }
  },
  '04: 2-Candidate Simple Plurality - 0.6000' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.6000
    }
  },
  '05: 2-Candidate Simple Plurality - 0.5500' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.5500
    }
  },
  '06: 2-Candidate Simple Plurality - 0.5400' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.5400
    }
  },
  '07: 2-Candidate Simple Plurality - 0.5300' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.5300
    }
  },
  '08: 2-Candidate Simple Plurality - 0.5200' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.5200
    }
  },
  '09: 2-Candidate Simple Plurality - 0.5100' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.5100
    }
  },
  '10: 2-Candidate Simple Plurality - 0.5050' : {
    'c' : ['A', 'B'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : 0.5050
    }
  },
  '11: 4-Candidate Simple Plurality' : {
    'c' : ['A', 'B', 'C', 'D'],
    'g' : simple_plurality_gen,
    'a' : simple_plurality_agg,
    'p' : {
      'nballots' : NBALLOTS,
      'ratio'    : None
    }
  },
  '13: 4-Candidate Mean Range Vote' : {
   'c' : ['A', 'B', 'C', 'D'],
   'g' : range_voting_gen,
   'a' : mean_range_voting_agg,
    'p' : {
      'nballots'  : NBALLOTS,
      'range_max' : RANGE_MAX
    }
  },
  '14: 4-Candidate Median Range Vote' : {
   'c' : ['A', 'B', 'C', 'D'],
   'g' : range_voting_gen,
   'a' : median_range_voting_agg,
    'p' : {
      'nballots'  : NBALLOTS,
      'range_max' : RANGE_MAX
    }
  }
}
