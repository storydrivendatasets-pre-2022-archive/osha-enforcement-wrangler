# OSHA Enforcement Data Catalog snapshotter


Downloads all the CSVs found here:

https://enforcedata.dol.gov/views/data_summary.php ([mirror](https://enforcedata.dol.gov/views/data_summary.php))

## Helpful references

- [Metadata for OSHA Enforcement Catalog (GSheets mirror)](https://docs.google.com/spreadsheets/d/1aHcSXSkPfUITRHE7Khsi-WuHbH2heYFXkb64DCRBiMo/edit#gid=1891906742)
- [Data dictionary for OSHA enforcement](https://docs.google.com/spreadsheets/d/1aHcSXSkPfUITRHE7Khsi-WuHbH2heYFXkb64DCRBiMo/edit#gid=0)


# TODOS

- [ ] Finish scripts/collect/stash_csvs.py
    - [X] Index configured files by year, when possible [decided no need for this]
    - [X] Don't numerically index single file groupings, unless they are more than ARBRITARY_FILE_SIZE_LIMIT, e.g. 20MB
- [ ] Compiling
    - [x] compile stashes into data/compiled/osha/raw
        - [x] normalize ld_dt and load_data to load_dt 
    - [x] sqlize data/compiled/osha/raw/*.csv to data/compiled/raw.sqlite
        - [x] Use apsw (takes ~4minutes; ~5min with blank-nulling)
        - [x] Blank should be set to NULL


- [ ] Wrangling
    - [ ] create data/sql/wrangled_schema.sql
    - [ ] Tidy/trim
        - [ ] How to use aspw to select from one db.table to create a table in another db
        - [ ] concatenate narrative data:
            - [ ] accident_abstract
            - [ ] violation_gen_duty_std
    - [ ] Fix boolean
    - [ ] rename columns?




