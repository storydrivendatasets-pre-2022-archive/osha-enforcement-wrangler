# Inventory of data

just informal tracking of how many records/unique ids exist for each table


## accident

### record count

```sql
SELECT COUNT(1) FROM accident;
# 134079
```


### summary_nr vs reporting_id

```sql
WITH tg AS (
    SELECT summary_nr, COUNT(1) FROM accident GROUP BY summary_nr
)
SELECT COUNT(1) 
FROM tg;
# unique summary_nr
# 134079  (same as record count)
```

```sql
WITH tg AS (
    SELECT reporting_id, COUNT(1) FROM accident GROUP BY reporting_id
)
SELECT COUNT(1) 
FROM tg;
# reporting_id
# 288 
#?????
```



### Number of summaries without corresponding accident_abstract

```sql
WITH xjoins AS (
    SELECT *
    FROM accident
    LEFT JOIN 
        accident_abstract 
        USING(summary_nr)
)
SELECT COUNT(1)
FROM xjoins
WHERE xjoins.abstract_text IS NULL
;
# 8, i.e. no abstract orphans
```

```sql
WITH xjoins AS (
    SELECT 
        tx.summary_nr
        , tx.reporting_id
        , tx.event_date
        , SUBSTR(tx.event_desc, 1, 15) AS event_desc
        , ty.abstract_text
    FROM accident AS tx
    LEFT JOIN 
        accident_abstract AS ty 
        USING(summary_nr)
)
SELECT summary_nr, reporting_id, event_date, event_desc
FROM xjoins
WHERE xjoins.abstract_text IS NULL
ORDER BY summary_nr ASC
;
```

| summary_nr | reporting_id | event_date       | event_desc      |
| ---------- | ------------ | ---------------- | --------------- |
| 100021534  | 214200       | 2002-04-17 11:40 |                 |
| 14223176   | 551800       | 1984-07-09 00:00 | FALL FROM LADDE |
| 142737     | 627100       | 1980-10-16 00:00 |                 |
| 201922663  | 626700       | 2003-01-13 16:30 | TWO EMPLOYEES K |
| 202522751  | 950624       | 2010-06-30 12:00 | EMPLOYEE AMPUTA |
| 220919468  | 257260       | 2016-12-27 07:12 | EMPLOYEE IS STR |
| 221231723  | 418800       | 2019-07-18 11:07 | EMPLOYEE IS ELE |
| 9407       | 112600       | 1984-03-25 00:00 |                 |





-------------------------------------


## accident_abstract

### record count

```sql
SELECT COUNT(1) FROM accident_abstract;
# 134072 (7 fewer than accidents)
```


### Number of summaries without corresponding accident.summary_nr

```sql
WITH xjoins AS (
    SELECT *
    FROM accident_abstract
    LEFT JOIN 
        accident 
        ON accident.summary_nr = accident_abstract.summary_nr
)
SELECT COUNT(1)
FROM xjoins
WHERE xjoins.reporting_id IS NULL
;
# 0, i.e. no abstract orphans
```

## inspection

### sic code vs naics_code

```sql
WITH codes AS (
    SELECT sic_code
        , COUNT(1) AS n
    FROM inspection
    GROUP BY sic_code
)
SELECT COUNT(1) FROM codes;

-- 1445 sic_code
```


```sql
WITH codes AS (
    SELECT naics_code
        , COUNT(1) AS n
    FROM inspection
    GROUP BY naics_code
)
SELECT COUNT(1) FROM codes;

-- 1269 sic_code
```



## violation


### Questions

- Why does `viol_type` have undocumented values of  U,F,P,H
