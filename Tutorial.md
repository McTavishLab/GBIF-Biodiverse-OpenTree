# GBIF-biodiverse-OpenTree
Linking data between GBIF, Biodiverse, and Open Tree of Life



The python scripts will rely on opentree and Dendropy.
To set up a virtual environment and install them run:

```
virtualenv -p python3 venv-gbot
source venv-gbot/bin/activate
pip install -r requirements.txt
```


Once that is set up - you can reactivate the environment any time you want to run analyses

```
source venv-gbot/bin/activate
```

Clone the example data and scripts using

```
git clone https://github.com/McTavishLab/GBIF-Biodiverse-OpenTree
cd GBIF-Biodiverse-OpenTree
```

## Taxon matching

To use OpenTree resources efficiently, you need to match you taxon names of interest to [Open Tree Taxonomy](https://tree.opentreeoflife.org/about/taxonomy-version/ott3.3) (OTT) ids.

There are several ways to do this:

- Web browser gui https://tree.opentreeoflife.org/curator/tnrs/ 

A demo file and detailed instruction at https://github.com/McTavishLab/jupyter_OpenTree_tutorials/blob/master/workbooks/OpenTree_workbook.ipynb


- TNRS APIs
Which can be accessed directly via: 
https://github.com/OpenTreeOfLife/germinator/wiki/Open-Tree-of-Life-Web-APIs#tnrs-methods 

Or you can use the TNRS via the R package ROTL, Quick start quide at https://github.com/ropensci/rotl#quick-start
 

Or using the python opentree package
https://opentree.readthedocs.io/en/latest/running_examples.html#tnrs


For the examples below, creat an output csv file, which is comma delimited and has a column containing ott_ids, labeled 'ott_id'


## Induced subtree

To get an induced subtree from synth for a set of opentree taxon ids:


e.g.

```
python scripts/induced_synth_subtree_from_csv.py -q tests/query.csv -o amphib_tree
```

Outputs will be written to the location specified by --output dir (default is synth_output)

Lablled_tree.txt: a tree in newick format tree containing these 100 taxa, and labelled internal nodes. 
Labels are by default 'name_and_id' Use flag 'label format' to select one of 'name', 'id', or 'name_and_id'"

ottid_dated_tree.tre: Dated tree with OTT ids as labels 
ott_label_dated_tree.tre: Dated tree with OTT names as labels.

Citations.txt: The citations of all the published trees inlcuded in the tree inference.
date_citations.txt: The citations of all the published trees used to infer dates.

synth.log: log file
ottlabel.tx, conflict_annot.tre,  support_annot.tre: Annotation files appropraite for viewing and annotating the tree on [itol](https://itol.embl.de/)


