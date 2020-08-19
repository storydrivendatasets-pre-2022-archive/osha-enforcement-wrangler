
# TODOS

## Priority 

- Need to read up on investigation process and find OSHA form 170:
    - 2005 history: https://www.osha.gov/enforcement/directives/cpl-02-00-137
    - https://www.osha.gov/report.html
    - https://www.osha.gov/pls/ser/serform.html Form No. OSHA 6-40.1.

- Read data definitions

    - inspection_detail: information: https://www.osha.gov/data/inspection-detail-definitions#tab1
    - inspection_detail: violation: https://www.osha.gov/data/inspection-detail-definitions#tab2
    - inspection_detail: accident https://www.osha.gov/data/inspection-detail-definitions#tab3
        - accident is more akin to "accident_investigation"
        - `summary_nr` may be a unique id for database purposes: 
     
            > Provides an unique identifier for the accident investigation. This investigation may be linked to several inspections, e.g., if there were multiple contractors at a construction site.



- [ ] Find/derive lookup table for accident codes...
    - [ ] violation-`standard` https://www.osha.gov/laws-regs/regulations/standardnumber
- [ ] Inspection and accident activity_nr AND summary_nr do not match up at all with webpage???: https://www.osha.gov/pls/imis/establishment.inspection_detail?id=1458614.015

## Current status


2020-08-19 reading/notes:
- maybe it helps if I think about the `accident` table as **investigation**, with a wholly unique `summary_nr` unconnected to ID numbers in the inspection table
    - an investigation can have multiple inspections
- maybe there is no connection between web app data IDs and the data?

2020-08-19 work:
- tried to hack more at OSHA data structure and its website. See 180-accident-injury-sql-together.md
- I'm stuck on this accident summary/investigation: https://www.osha.gov/pls/imis/establishment.inspection_detail?id=1437294.015
    - has summary NR of 121039.015
    - But in the database, the corresponding accident has summary_nr of: 221210396 




- should investigate individual records, come up with story queries (am struggling with this)
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

