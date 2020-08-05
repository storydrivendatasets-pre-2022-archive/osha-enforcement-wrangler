# Useful views to generate

## Left join accidents with corresponding accident_abstract

All but **8** accident records have a corresponding accident_abstract

```sql
SELECT 
accident.*
, accident_abstract.abstract_text AS abstract_text
, accident_abstract.line_count AS abstract_line_count 
FROM accident
LEFT JOIN 
    accident_abstract 
    USING(summary_nr);
```

## Join inspections with related_activity

```sql
SELECT *
FROM inspection
INNER JOIN 
    related_activity 
    ON related_activity.activity_nr = inspection.activity_nr
--        AND related_activity.rel_type = 'I'
INNER JOIN
    accident
    ON accident.summary_nr = related_activity.rel_act_nr
        AND related_activity.rel_type = 'A'
;    



```
