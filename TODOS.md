
# TODOS

## Priority 

- [ ] Find/derive lookup table for accident codes...
    - [ ] violation-`standard` https://www.osha.gov/laws-regs/regulations/standardnumber
- [ ] Inspection and accident activity_nr AND summary_nr do not match up at all with webpage???: https://www.osha.gov/pls/imis/establishment.inspection_detail?id=1458614.015

## Current status


- should investigate individual records, come up with story queries
- [ ] haven't decided if i should use virtual tables/ft5 for full text search on accident_abstract and violation_gen_duty_std
        ```sql
        -- CREATE VIRTUAL TABLE IF NOT EXISTS "accident_abstract_vt" USING fts5 (
        --   "summary_nr",
        --   "line_count",
        --   "abstract_text",
        --   "load_dt"
        -- );
        ```


## most recently done

- [x] added collate nocase to table creation statements
- [X] Wrangled DB is properly indexed
- [X] factor out stash step for separate datastash repo
- [x] Maybe re-insert accident_abstract to do group concat with space char instead of no char?


## General

- [?] write a new logger

## Wrangling



- Indexing
    - [tk] Index all tables in wrangled
    - [X] Add primary key
    - [ ] Add foreign key

- zeropadding
    - [X] activity_nr, summary_nr needs to be zeropadded to 9 digits
    - [X] citation_id, reporting_id needs to be zeropadded to 7 digits
    - [X] zipcodes in inspection

- [ ] Check integrity/accuracy of data/wrangled/osha_wrangled.sqlite

In [notes](notes/notes-wrangle-update-transform-data.md)


### Updating/transforms

- [ ] in violation, group concat hazsub1-5
    - do all rows with hazsub2 have hazsub1 filled in, etc?
    - group count of hazsub? 


## Repo reorg

- [X] Take the "Stash" step out of the main Make
    - [X] compile step should read directly from unpacked
- [X] Add metadata to table definition
    - all TEXT fields are CHAR/VARCHAR
    - added comments when necessary

- [ ] create separate repo for stashed data

- [ ] Create a osha_enum lookup table
    - violation_event,hist_event, hist_vtype, pen_fta
    - accident.report_id (reporting jurisdictions)

## Overall questions and other work

- [ ] What is violation_event.hist_insp_nr? Most are null

