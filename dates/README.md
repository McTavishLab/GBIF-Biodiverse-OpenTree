I ran these estimates using Chronosynth https://github.com/OpenTreeOfLife/chronosynth/tree/dev
to get node age estimates from input trees in the OpenTree datastore Phylesystem.

Hypothetically, anyone could run them as well.
In practice, the configuration is a bit finicky and dates database is a bit sluggish to get up and running.
But I'm working on tidying it up!


python ../../scripts/label_and_date_tree.py  -q ../../data/mammals.csv --output mammal.tre
python ../../scripts/label_and_date_tree.py  -q ../../data/amphibians.csv --output amph.tre
python ../../scripts/label_and_date_tree.py  -q ../../data/reptiles.csv --output reptiles.tre
python ../../scripts/label_and_date_tree.py  -q ../../data/Fabaceae_in_AU.csv --output AU_Fab.tre


Where dates for the age of the clade weren't found in the database, I had to pass ones in, 
(these ones are based on a quick google search)

python ../../scripts/label_and_date_tree.py  -q ../../data/birds.csv --max_age 75 --output birds.tre
python ../../scripts/label_and_date_tree.py  -q ../../data/gymnosperms.csv --max_age 285 --output gymno.tre
