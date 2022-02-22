# GBIF-biodiverse-OpenTree
Linking data between GBIF, Biodiverse, and Open Tree of Life



The python scripts will rely on opentree and Dendropy.
To set up a virtual environment and install them run:

```
virtualenv -p python3 venv-gbot
source venv-gbot/bin/activate
pip install -r requirements.txt
```


Once that is set up - you can reactivate using any time you want to run analyses

```
source venv-gbot/bin/activate
```

To get an induced subtree from synth for a set of opentree ids:
```
python scripts/induced_synth_subtree_from_csv.py -q tests/query.csv
```