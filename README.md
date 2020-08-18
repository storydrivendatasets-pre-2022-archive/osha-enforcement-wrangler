# OSHA Enforcement Data Catalog wrangler


Downloads all the CSVs found here:

https://enforcedata.dol.gov/views/data_summary.php ([mirror](https://enforcedata.dol.gov/views/data_summary.php))

And compiles and wrangles into a handy SQLite database




## How to fetch and compile the data with this repo

```sh
# make a work directory of your choice
mkdir -p worky && cd worky

# clone this repo into a subdir named osha_wrangler
git clone https://github.com/storydrivendatasets/osha-enforcement-wrangler \
    osha_wrangler

cd osha_wrangler

# install the Python 3.7+ requirements
pip install -r requirements.txt

# run the task to collect fresh data
make collect

# run the task to compile the raw text into a SQLite database at:
# data/compiled/osha_compiled.sqlite
make compile

# run the task to wrangle the compiled DB into a wrangled "final" SQLite DB at:
# data/wrangled/osha_wrangled.sqlite
make wrangle
```

## Walkthroughs

- [DRAFT: Looking at an injury accident investigation](walkthroughs/single-accident-inspection/index.md) on the OSHA online web database and in SQL exploration of `data/wrangled/osha_wrangled.sqlite`


## Helpful references

- [Metadata for OSHA Enforcement Catalog (GSheets mirror)](https://docs.google.com/spreadsheets/d/1aHcSXSkPfUITRHE7Khsi-WuHbH2heYFXkb64DCRBiMo/edit#gid=1891906742)
- [Data dictionary for OSHA enforcement](https://docs.google.com/spreadsheets/d/1aHcSXSkPfUITRHE7Khsi-WuHbH2heYFXkb64DCRBiMo/edit#gid=0)

OSHA reference for accident/violation/inspection definitions:
https://www.osha.gov/data/inspection-detail-definitions#tab2


