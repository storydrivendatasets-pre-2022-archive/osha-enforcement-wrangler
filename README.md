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
    - [ ] Blank should be set to NULL
    - [ ] Fix boolean
    - [ ] concatenate narrative data:
        - [ ] accident_abstract
        - [ ] violation_gen_duty_std
    - [ ] trim unnecessary fields
    - [ ] rename columns: data/cache/lookups/osha_header_renames.csv
    - [ ] 

## Trimming the compiled data

```sh
find data/compiled/osha/raw/*.csv | while read -r fname; do
    echo ""
    echo "-----------------"
    echo "$fname"
    head -n 100000 "$fname" | xsv count
    head -n 100000 "$fname" | xsv frequency | xsv search 'NULL'
done
```


### Are any load_dt's between related reports out of sync?



### accident

- always null: abstract_text, event_time, state_flag
- event_date trim seconds value

### accident_abstract
- connects to accident via summary_nr

### accident_injury
- always null: fall_distance
- not needed?: line_nr – since we concat all the lines in accident_abstract

### accident_lookup2
- load_dt: load_date
- rename table to accident_lookup

### inspection
- always null: state_flag
- bool ('X' vs BLANK): safety_manuf,safety_const,safety_marit,safety_manuf,health_const,health_marit,migrant
- bool Y/N/NULL: adv_notice
- load_dt: ld_dt

### optional_info
(in spreadsheet)

### related_activity
- bool: rel_safety, rel_health

### strategic codes

### violation
- bool: emphasis,delete_flag

### violation_event

### violation_gen_duty_std
