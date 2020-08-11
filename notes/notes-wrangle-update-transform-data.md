
# Wrangling

## insert/import TODOs

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

## update/transform TODOs

- [x] drop unnecessary load_dt?
    - removing ALL load_dt saves 500MB
    - removing a few saves 70MB

- Updating
    - [X] truncate all load_dt to just a date (or do it in the INSERT INTO?)
    - [X] Write pythonsql function to make_boolean out of 'Y', 'N', etc
    - [x] normalize casing of site_city, site_address with NORMALIZE_TEXT custom function

- rename columns?
    - [ ] inspection.reporting_id to report_id

- lookups
    - [ ] sics to naics crosswalk: https://www.naics.com/sic-naics-crosswalk-search-results

- Crosswalk tables
    - [ ] Create crosswalk_accident_report_id, via accident.report_id
    - [ ] Create crosswalk_accident_event_keyword, via accident.event_keyword:
            summary_nr, event_keyword
    - [ ] Create crosswalk_accident_sic_codes, via accident.sic_list
    - [ ] 


--------

# Questions

# What do these table fields mean?





# Tricks

## How to pull a list of delimited keywords using recursive SQL

http://www.samuelbosch.com/2018/02/split-into-rows-sqlite.html

```sql


WITH RECURSIVE 
    rx(summary_nr, keyword, kstring) 
    AS (
        SELECT
            summary_nr
            , ''
            , event_keyword || ','
        FROM accident
        UNION ALL
        SELECT summary_nr
            , SUBSTR(kstring, 0, INSTR(kstring, ','))
            , SUBSTR(kstring, INSTR(kstring, ',') + 1)
        FROM rx
        WHERE kstring <> ''        
)
SELECT 
    summary_nr
    , keyword
FROM rx 
WHERE keyword <> ''
ORDER BY 
    summary_nr ASC
    , keyword ASC
;


```



## More recursive fun

```sql
SELECT 
    seqno AS idx_seqno
    , cid AS idx_cid
    , name AS idx_name
FROM 
    PRAGMA_INDEX_INFO("accident")
```

```sql
SELECT 
    name AS col_name
FROM
    PRAGMA_INDEX_LIST("accident")
```

```sql


WITH tx AS (
    SELECT 
        name AS table_name 
    FROM sqlite_master WHERE type='table'
    ORDER BY table_name ASC
), rx AS (
    SELECT
        tx.table_name
        , pg.name AS index_name
    FROM tx
    INNER JOIN    
        PRAGMA_INDEX_LIST(tx.table_name) AS pg
), ry AS (
    SELECT rx.table_name
        , rx.index_name
        , pg.cid
        , pg.seqno
        , pg.name AS col_name
    FROM rx
    INNER JOIN        
        PRAGMA_INDEX_INFO(rx.index_name) AS pg    
    ORDER BY 
        table_name ASC 
        , cid ASC
        , seqno ASC
)
SELECT
    table_name
    , index_name
    , GROUP_CONCAT(col_name, '|') AS indexcols
FROM ry
GROUP BY 
    table_name
    , index_name
;
```


