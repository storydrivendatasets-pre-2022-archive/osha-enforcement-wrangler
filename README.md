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
    - Migration/create/insert into logistics
        - [O] How to use aspw to select from one db.table to create a table in another db?
        - [O] Or do I just want to do a CREATE AS statement, which removes the NOT NULL constraint? https://www.techonthenet.com/sqlite/tables/create_table_as.php
        - [X] or create data/sql/wrangled_schema.sql
        - [X] create each individual INSERT INTO statement
            - [X] concatenate narrative data:
                - [X] accident_abstract
                    ```sh
                    SELECT 
                        summary_nr
                        , COUNT(1) as line_count
                        , GROUP_CONCAT(abstract_text, '') AS abstract_text
                        , MAX(load_dt) AS load_dt
                    FROM accident_abstract
                    GROUP BY summary_nr
                    HAVING line_count > 1
                    ```
                - [X] violation_gen_duty_std

    - Updating
        - [X] truncate all load_dt to just a date (or do it in the INSERT INTO?)
        - [X] Write pythonsql function to make_boolean out of 'Y', 'N', etc
    - [ ] rename columns?
    - [ ] drop unnecessary load_dt?
        - removing ALL load_dt saves 500MB


## Overall questions and other work

- [ ] Create a osha_enum lookup table
    - violation_event,hist_event, hist_vtype, pen_fta

- [ ] What is violation_event.hist_insp_nr? Most are null
- [ ] Add metadata to table definition
