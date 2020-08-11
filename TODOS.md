
# TODOS


## Current status

- Wrangled DB is properly indexed
- should investigate individual records, come up with story queries
- factor out stash step for separate datastash repo

## General

- [ ] write a new logger

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

