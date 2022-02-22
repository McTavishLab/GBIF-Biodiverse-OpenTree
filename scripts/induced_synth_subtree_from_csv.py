#!/usr/bin/env python3
"""
to run:
python induced_synth_subtree_from_csv.py --query ../tests/query.csv --outfile tree.nwk

-ott-ids data file should have a column containing ott_ids, labeled 'ott_id', and be either comm
"""

import argparse
import os
from opentree.taxonomy_helpers import labelled_induced_synth


parser = argparse.ArgumentParser()
parser.add_argument("-q","---query", help="File containing ott_ids. First should have the header 'ott_id' and contain OpenTree taxon ids")
parser.add_argument("-o","--output", default="output.tre", help="output file. default is output.tre")
parser.add_argument("-l","--label_format", default="name_and_id",help="label format. One of 'name', 'id', 'name_and_id'. Default is 'name_and_id'")

args = parser.parse_args()


assert os.path.exists(args.query)

queryfile = open(args.query)
header = queryfile.readline()
assert header.split(',')[0] == 'ott_id'

ott_ids=set()
for lin in queryfile.readlines():
    lii = lin.split(',')
    ott_ids.add(lii[0])


ott_ids = list(ott_ids)
ret = labelled_induced_synth(ott_ids = ott_ids,
                                                       label_format = args.label_format, 
                                                       inc_unlabelled_mrca=False, 
                                                       standardize=True)

ret['labelled_tree'].write(path=args.output, schema='newick')