# OSHA Enforcement Data Catalog snapshotter


Downloads all the CSVs found here:

https://enforcedata.dol.gov/views/data_summary.php ([mirror](https://enforcedata.dol.gov/views/data_summary.php))


# TODOS

- [ ] Finish scripts/collect/stash_csvs.py
    - [X] Index configured files by year, when possible [decided no need for this]
    - [X] Don't numerically index single file groupings, unless they are more than ARBRITARY_FILE_SIZE_LIMIT, e.g. 20MB
- [ ] Compiling
    - [x] compile stashes into data/compiled/osha/raw
    - [x] sqlize data/compiled/osha/raw/*.csv to data/compiled/raw.sqlite
        - [x] Use apsw (takes ~4minutes)

- [ ] Wrangling
    - [ ] figure out unnecessary fields
    - [ ] trim unnecessary fields
    - [ ] concatenate narratives (sql?)
